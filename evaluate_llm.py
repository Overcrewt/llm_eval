import json
import os
import re
from huggingface_hub import hf_hub_download
from llama_cpp import Llama
from tqdm import tqdm

def get_evaluator_model():
    print("Downloading/Locating evaluator model (Meta-Llama-3-8B-Instruct)...")
    repo_id = "QuantFactory/Meta-Llama-3-8B-Instruct-GGUF"
    filename = "Meta-Llama-3-8B-Instruct.Q4_K_M.gguf"
    return hf_hub_download(repo_id=repo_id, filename=filename)

def get_metadata():
    print("\n--- Please enter the evaluated model's metadata ---")
    metadata = {}
    metadata["Model Name"] = input("Model Name: ").strip()
    metadata["URL"] = input("Hugging Face URL: ").strip()
    metadata["Parameters Count"] = input("Parameters Count: ").strip()
    metadata["Base Architecture"] = input("Base Architecture (e.g., Llama-2, Mistral): ").strip()
    metadata["Type"] = input("Type (e.g., Instruct, Chat, Base): ").strip()
    metadata["Number of Downloads"] = input("Number of Downloads: ").strip()
    metadata["Date of Last Update"] = input("Date of Last Update: ").strip()
    metadata["Available Quantization Formats"] = input("Available Quantization Formats: ").strip()
    metadata["Other Info"] = input("Other Info: ").strip()
    return metadata

def parse_json_response(text):
    # Try to extract json block from text
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        return json.loads(text)
    except json.JSONDecodeError:
        return None

def evaluate():
    model_path = get_evaluator_model()
    print("Loading evaluator model...")
    llm = Llama(model_path=model_path, n_ctx=4096, n_gpu_layers=-1, verbose=False)

    metadata = get_metadata()

    # Load questions
    with open("questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)

    # Load answers.json
    reference_answers = {}
    if os.path.exists("answers.json"):
        with open("answers.json", "r", encoding="utf-8") as f:
            ans_data = json.load(f)
            for a in ans_data:
                reference_answers[a["id"]] = a["answer"]

    # Combine with reference answers inside questions.json
    for q in questions:
        if "reference_answer" in q:
            reference_answers[q["id"]] = q["reference_answer"]

    # Load model answers
    if not os.path.exists("answers_llm.json"):
        print("answers_llm.json not found! Run ask_llm.py first.")
        return

    with open("answers_llm.json", "r", encoding="utf-8") as f:
        model_answers_data = json.load(f)

    model_answers = {a["id"]: a["answer"] for a in model_answers_data}

    results = []

    for q in tqdm(questions, desc="Evaluating Answers"):
        qid = q["id"]
        question_text = q["question"]
        ref_ans = reference_answers.get(qid, "No reference answer provided.")
        mod_ans = model_answers.get(qid, "")

        if not mod_ans:
            print(f"Skipping {qid} because no model answer was found.")
            continue

        if qid in ["Q16", "Q17", "Q18", "Q19"]:
            prompt = f"""You are an expert cybersecurity evaluator.
Your task is to evaluate an LLM's response to a code review question based on a reference answer.

[Question]
{question_text}

[Reference Answer]
{ref_ans}

[Model Answer]
{mod_ans}

Evaluate the Model Answer based on the trap scoring criteria:
- Level 1 only = score 2.
- Levels 1+2 = score 4.
- All three levels (1, 2, 3) = score 5.
- Missing Level 1 = score 1.

Provide a short breakdown/reasoning, and strictly output in the following JSON format:
{{
    "Code Review Trap Score": <score>,
    "Reasoning": "<short reasoning>"
}}"""
        elif qid in ["Q20", "Q21", "Q22", "Q27"]:
            prompt = f"""You are an expert cybersecurity evaluator.
Your task is to evaluate an LLM's response to a hallucination trap question.

[Question]
{question_text}

[Reference Answer]
{ref_ans}

[Model Answer]
{mod_ans}

Evaluate the Model Answer based on the hallucination trap scoring criteria:
- If the model correctly identifies the trap (says "I don't know" or corrects the false information) = score 5.
- If the model partially falls for it = score 2.
- If the model confidently fabricates an answer = score 1.

Provide a short breakdown/reasoning, and strictly output in the following JSON format:
{{
    "Hallucination Trap Score": <score>,
    "Reasoning": "<short reasoning>"
}}"""
        else:
            prompt = f"""You are an expert cybersecurity evaluator.
Your task is to evaluate an LLM's response to a cybersecurity question based on a reference answer.

[Question]
{question_text}

[Reference Answer]
{ref_ans}

[Model Answer]
{mod_ans}

Evaluate the Model Answer according to the following criteria (1-5):
- Technical Accuracy: 5=Fully correct, 4=Minor inaccuracies, 3=Mix of correct/incorrect, 2=Significant errors, 1=Mostly/entirely incorrect.
- Completeness: 5=Comprehensive, 4=Covers main points, 3=Partially complete, 2=Superficial, 1=Minimal/empty.
- Practical Applicability: 5=Directly usable, 4=Usable with minor adjustments, 3=Provides starting point, 2=Not usable without rewriting, 1=Not applicable/wrong.

Provide a short breakdown/reasoning, and strictly output in the following JSON format:
{{
    "Technical Accuracy": <score>,
    "Completeness": <score>,
    "Practical Applicability": <score>,
    "Reasoning": "<short reasoning>"
}}"""

        messages = [
            {"role": "system", "content": "You are a helpful JSON-outputting evaluator assistant."},
            {"role": "user", "content": prompt}
        ]

        try:
            response = llm.create_chat_completion(
                messages=messages,
                max_tokens=500,
                temperature=0.1,
                response_format={"type": "json_object"}
            )
            eval_text = response["choices"][0]["message"]["content"]
            eval_data = parse_json_response(eval_text)
            
            if not eval_data:
                eval_data = {"Reasoning": "Failed to parse evaluator response.", "Error": True}
        except Exception as e:
            eval_data = {"Reasoning": f"Evaluator threw an error: {e}", "Error": True}

        results.append({
            "id": qid,
            "question": question_text,
            "evaluation": eval_data
        })

    # Append to report.md
    report_file = "report.md"
    mode = "a" if os.path.exists(report_file) else "w"
    
    with open(report_file, mode, encoding="utf-8") as f:
        f.write(f"\n## Model Evaluation: {metadata['Model Name']}\n\n")
        f.write("### Metadata\n")
        for k, v in metadata.items():
            f.write(f"- **{k}:** {v}\n")
        f.write("\n### Scores Breakdown\n\n")
        
        # Build table header based on all possible keys
        f.write("| Question ID | Technical Accuracy | Completeness | Practical Applicability | Trap Score | Reasoning |\n")
        f.write("|---|---|---|---|---|---|\n")
        
        for res in results:
            qid = res["id"]
            ev = res["evaluation"]
            
            ta = ev.get("Technical Accuracy", "-")
            comp = ev.get("Completeness", "-")
            pa = ev.get("Practical Applicability", "-")
            
            trap_score = ev.get("Code Review Trap Score", ev.get("Hallucination Trap Score", "-"))
            
            reasoning = ev.get("Reasoning", "").replace("\n", " ") # Keep in one line for table
            
            f.write(f"| {qid} | {ta} | {comp} | {pa} | {trap_score} | {reasoning} |\n")
        
        f.write("\n---\n")

    print(f"Evaluation complete! Results appended to {report_file}")

if __name__ == "__main__":
    evaluate()
