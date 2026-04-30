import json
import re
import os
from huggingface_hub import hf_hub_download
from llama_cpp import Llama
from tqdm import tqdm

def download_model_from_url(url):
    # Example: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_K_M.gguf
    match = re.search(r"huggingface\.co/([^/]+/[^/]+)/(?:blob|resolve)/[^/]+/(.+)", url)
    if not match:
        raise ValueError("Invalid Hugging Face URL. Expected format: https://huggingface.co/<repo_id>/blob/main/<filename>")
    
    repo_id = match.group(1)
    filename = match.group(2)
    print(f"Downloading/Locating {filename} from {repo_id}...")
    return hf_hub_download(repo_id=repo_id, filename=filename)

def main():
    url = input("Enter the Hugging Face URL for the GGUF model: ").strip()
    try:
        model_path = download_model_from_url(url)
    except Exception as e:
        print(f"Error downloading model: {e}")
        return

    print("Loading model...")
    # Using n_gpu_layers=-1 to offload all layers to GPU (ideal for DigitalOcean GPU droplets)
    try:
        llm = Llama(model_path=model_path, n_ctx=4096, n_gpu_layers=-1, verbose=False)
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    questions_file = "questions.json"
    answers_file = "answers_llm.json"

    if not os.path.exists(questions_file):
        print(f"Could not find {questions_file}")
        return

    with open(questions_file, "r", encoding="utf-8") as f:
        questions = json.load(f)

    # Load existing answers to resume if interrupted
    answers = []
    answered_ids = set()
    if os.path.exists(answers_file):
        try:
            with open(answers_file, "r", encoding="utf-8") as f:
                answers = json.load(f)
                answered_ids = {a["id"] for a in answers}
        except json.JSONDecodeError:
            print("Could not read existing answers_llm.json. Starting fresh.")

    for q in tqdm(questions, desc="Asking Questions"):
        if q["id"] in answered_ids:
            continue
            
        messages = [
            {"role": "system", "content": "You are a helpful, knowledgeable cybersecurity expert."},
            {"role": "user", "content": q["question"]}
        ]
        
        try:
            # Try using chat completion (relies on model having a chat template in GGUF metadata)
            response = llm.create_chat_completion(
                messages=messages,
                max_tokens=1024,
                temperature=0
            )
            answer_text = response["choices"][0]["message"]["content"].strip()
        except Exception as e:
            # Fallback for base models without a chat template
            prompt = f"System: You are a helpful, knowledgeable cybersecurity expert.\nUser: {q['question']}\nAssistant: "
            response = llm(
                prompt,
                max_tokens=1024,
                temperature=0.2,
                stop=["User:", "System:"]
            )
            answer_text = response["choices"][0]["text"].strip()
            
        answers.append({
            "id": q["id"],
            "answer": answer_text
        })
        
        # Save progressively
        with open(answers_file, "w", encoding="utf-8") as f:
            json.dump(answers, f, indent=4)

    print(f"\nCompleted! Answers saved to {answers_file}")

if __name__ == "__main__":
    main()
