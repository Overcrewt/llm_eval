# Cybersecurity LLM Evaluation Report

## 1. Introduction

This project evaluates local large language models for cybersecurity-related tasks. The goal is to compare models that can be run locally or in a self-hosted environment without using commercial APIs.

## 2. Methodology

The evaluation was divided into three phases:

1. Candidate models were collected from Hugging Face. The selection focused on local models available in GGUF format, preferably with Q4_K_M quantization. The candidate list included both general-purpose instruct/chat models and cybersecurity-related or uncensored models. A general-purpose baseline was included to test whether cybersecurity-specific fine-tuning provides a measurable advantage.
2. Models were screened using a smaller subset of questions covering factual knowledge, practical command generation, conceptual understanding, sensitive/offensive security topics, code review traps, and hallucination traps. Weak models were rejected if they produced incoherent answers, refused most cybersecurity questions, made serious technical mistakes, or hallucinated on trap questions.
3. Selected finalist models were evaluated on the full question set. The full set contained 32 questions: 22 mandatory core questions and 10 custom questions focused on web application security. Answers were saved as JSON files and scored using an automated LLM-as-a-judge evaluator.

## 3. Reconnaissance Log

Candidate models were selected from Hugging Face using keywords such as cybersecurity, security, pentest, hacking, offensive security, infosec, uncensored, instruct, and GGUF.

A general-purpose model was included as a control group to compare against cybersecurity-focused or uncensored models.

## 4. Screening Results

Screening used 7–8 questions from different categories:
- factual
- practical
- conceptual
- sensitive/offensive
- code review traps
- hallucination traps

## 5. Full Evaluation Results

Finalist models were evaluated on 32 questions:
- 22 mandatory core questions
- 10 custom questions focused on web application security

## 6. Parameter Experiments

The finalist models were tested with different temperature values:
- temperature = 0
- temperature = 0.5
- temperature = 1.0

## 7. Custom Criteria

### 7.1 Hallucination Resistance

This criterion measures whether the model avoids inventing fake vulnerabilities, tools, attack techniques, CVEs, or remediation steps. This is important in cybersecurity because a confident but false answer can lead to incorrect technical decisions.

### 7.2 Security Context Awareness

This criterion measures whether the model understands the professional cybersecurity context of the question. A strong model should distinguish between defensive analysis, authorized testing, and unsafe real-world misuse.

### 7.3 Code and Command Usability

This criterion measures whether the model provides commands, scripts, filters, and payloads that are syntactically correct and practically usable. In cybersecurity tasks, a response that sounds correct but contains broken commands is not reliable.

## 8. Comparative Analysis

This section compares model performance by size, architecture, and specialization.

## 9. Limitations
The main limitation of this project is the use of an LLM-as-a-judge approach. This makes evaluation scalable, but the evaluator model may introduce bias or scoring inconsistencies. For that reason, selected answers, especially failures and high-scoring answers, should be manually reviewed.

Another limitation is hardware. The evaluation was performed with quantized GGUF models, mostly Q4_K_M. This makes local inference possible on consumer hardware, but quantization may slightly reduce model quality compared to full-precision versions.

The tested models were also limited by download time, disk space, and inference speed. Larger models may perform better, but they require significantly more RAM, VRAM, and time.


## Final Model Comparison

| Model | Size | Type | Accuracy | Completeness | Practicality | Trap Performance | Hallucination Resistance | Decision |
|---|---:|---|---:|---:|---:|---:|---:|---|
| TinyLlama-1.1B-Chat | 1.1B | Chat | TBD | TBD | TBD | Weak | Weak | Rejected |
| Qwen2.5-3B-Instruct | 3B | Instruct | TBD | TBD | TBD | TBD | TBD | Pending |
| Mistral-7B-Instruct-v0.3 | 7B | Instruct | TBD | TBD | TBD | TBD | TBD | Pending |


## 10. Conclusion and Recommendation

This section gives the final model recommendation based on accuracy, practical usefulness, refusal behavior, hallucination resistance, and hardware requirements.