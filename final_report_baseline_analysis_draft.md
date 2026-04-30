# Cybersecurity LLM Evaluation Report

## 1. Introduction

This project evaluates local large language models for cybersecurity-related tasks. The goal is to compare models that can be run locally or in a self-hosted environment without using commercial APIs.

The assignment focuses on a practical question: whether local LLMs can provide useful cybersecurity answers while remaining technically accurate. A model that is willing to answer offensive-security questions is not automatically useful. It must also avoid hallucinations, produce correct commands, and identify vulnerabilities accurately.

## 2. Methodology

The evaluation was divided into three phases.

First, candidate models were collected from Hugging Face. The selection focused on local models available in GGUF format, preferably with Q4_K_M quantization. The candidate list included general-purpose instruct/chat models, coder models, and cybersecurity-related fine-tunes. A general-purpose baseline was included to test whether cybersecurity-specific fine-tuning provides a measurable advantage.

Second, models were screened using questions from multiple categories: factual knowledge, practical command generation, conceptual understanding, sensitive/offensive security topics, code review traps, and hallucination traps. Models were rejected if they produced incoherent answers, gave many unusable commands, failed most hallucination traps, or did not provide a useful comparison point.

Third, the selected models were evaluated on the full question set. The full set contained 32 questions: 22 mandatory core questions and 10 custom questions focused on web application security. Raw model answers were saved as JSON files and scored using an automated LLM-as-a-judge evaluator.

All baseline runs used:
- GGUF models
- mostly Q4_K_M quantization
- llama-cpp-python
- local RTX/CUDA acceleration
- context length: 4096 tokens
- temperature: 0 for the baseline evaluation

## 3. Reconnaissance Log

Candidate models were selected from Hugging Face using keywords such as cybersecurity, security, pentest, hacking, offensive security, infosec, uncensored, instruct, coder, and GGUF.

The evaluated set included small models, 7B-class models, cybersecurity-focused models, and larger 9B–12B models. This made it possible to compare model size, architecture, specialization, and hardware cost.

The tested or attempted models included:

| Model | Overall Avg | Trap Avg | Decision |
|---|---|---|---|
| TinyLlama-1.1B-Chat-v1.0 | 2.97 | 1.89 | Rejected |
| Qwen2.5-3B-Instruct | 3.99 | 4.22 | Finalist |
| Mistral-7B-Instruct-v0.3 | 4.05 | 3.33 | Finalist |
| Llama-3.2-3B-Instruct | 3.93 | 4.22 | Rejected / backup |
| Phi-3.5-mini-instruct | 4.01 | 4.22 | Finalist |
| PHI-4-MINI-INSTRUCT |  |  | Skipped |
| Qwen2.5-7B-Instruct | 3.99 | 4.00 | Rejected / backup |
| Qwen2.5-Coder-7B-Instruct | 4.08 | 3.67 | Finalist |
| WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B | 4.04 | 3.56 | Finalist |
| Lily-Cybersecurity-7B-v0.2 | 3.94 | 3.00 | Rejected |
| SenecaLLM_x_Qwen2.5-7B-CyberSecurity | 4.00 | 3.67 | Rejected / backup |
| Gemma-2-9B-it | 3.97 | 4.11 | Rejected / backup |
| Mistral-Nemo-Instruct-2407 | 4.36 | 3.78 | Finalist |

`PHI-4-MINI-INSTRUCT` was skipped because it downloaded but failed to load with the current CUDA backend.

## 4. Screening Results

The screening phase showed clear differences between models.

TinyLlama was useful only as a baseline. It was fast and small, but it had weak practical command quality and poor hallucination-trap performance.

Qwen2.5-3B-Instruct and Phi-3.5-mini-instruct were the strongest small models. Both produced good general answers while requiring much less hardware than larger models.

Mistral-7B-Instruct-v0.3 was a strong general-purpose 7B baseline with good normal and practical scores, but weaker hallucination resistance.

Qwen2.5-Coder-7B-Instruct was one of the strongest practical/code models. It performed well on command generation and code review tasks, but still hallucinated on some fake vulnerability prompts.

WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B was selected as a cybersecurity/coder finalist to compare domain-oriented tuning against general and coder models.

Mistral-Nemo-Instruct-2407 had the best overall score and the strongest practical subset score, but it also had the highest hardware cost.

The selected finalists were:
1. Qwen2.5-3B-Instruct
2. Phi-3.5-mini-instruct
3. Mistral-7B-Instruct-v0.3
4. Qwen2.5-Coder-7B-Instruct
5. WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B
6. Mistral-Nemo-Instruct-2407

## 5. Full Evaluation Results

The automated scoring output is stored in `report.md`. The summary below was generated from the full report.

| Model | Normal Avg | Trap Avg | Overall Avg | Factual | Practical | Code Traps | Hallucination |
|---|---|---|---|---|---|---|---|
| TinyLlama-1.1B-Chat-v1.0 | 3.12 | 1.89 | 2.97 | 3.33 | 2.50 | 2.60 | 1.00 |
| Qwen2.5-3B-Instruct | 3.96 | 4.22 | 3.99 | 4.12 | 3.83 | 4.80 | 3.50 |
| Mistral-7B-Instruct-v0.3 | 4.14 | 3.33 | 4.05 | 4.12 | 4.38 | 4.80 | 1.50 |
| Llama-3.2-3B-Instruct | 3.89 | 4.22 | 3.93 | 4.08 | 3.95 | 5.00 | 3.25 |
| Phi-3.5-mini-instruct | 3.99 | 4.22 | 4.01 | 4.12 | 3.79 | 5.00 | 3.25 |
| PHI-4-MINI-INSTRUCT |  |  |  |  |  |  |  |
| Qwen2.5-7B-Instruct | 3.99 | 4.00 | 3.99 | 4.00 | 3.79 | 5.00 | 2.75 |
| Qwen2.5-Coder-7B-Instruct | 4.13 | 3.67 | 4.08 | 4.04 | 4.54 | 5.00 | 2.00 |
| WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B | 4.10 | 3.56 | 4.04 | 3.96 | 4.17 | 4.80 | 2.00 |
| Lily-Cybersecurity-7B-v0.2 | 4.06 | 3.00 | 3.94 | 4.08 | 4.17 | 4.60 | 1.00 |
| SenecaLLM_x_Qwen2.5-7B-CyberSecurity | 4.04 | 3.67 | 4.00 | 4.00 | 4.50 | 4.80 | 2.25 |
| Gemma-2-9B-it | 3.96 | 4.11 | 3.97 | 4.12 | 3.75 | 5.00 | 3.00 |
| Mistral-Nemo-Instruct-2407 | 4.43 | 3.78 | 4.36 | 4.29 | 4.71 | 5.00 | 2.25 |

Main result:
- Mistral-Nemo-Instruct-2407 had the highest overall average.
- Qwen2.5-Coder-7B-Instruct had the strongest role among code-focused 7B models.
- Qwen2.5-3B-Instruct and Phi-3.5-mini-instruct were the strongest small models.
- TinyLlama was rejected because of weak practical answers and very poor hallucination resistance.

## 6. Parameter Experiments

Baseline temperature = 0 testing has been completed.

TODO:
Run the finalist models at:
- temperature = 0.5
- temperature = 1.0

The most important questions to compare across temperatures are:
- Q20–Q22: hallucination traps
- Q27: fake PhantomHeader vulnerability
- Q24 and Q30: practical offensive-security tasks
- Q32: precise secure Java XML parser configuration

Expected analysis:
- Higher temperature may make answers longer and more varied.
- Higher temperature may increase hallucination risk.
- Code and command answers may become less consistent at temperature = 1.0.
- Temperature should matter most on hallucination traps and practical code/payload questions.

## 7. Custom Criteria

### 7.1 Hallucination Resistance

This criterion measures whether the model avoids inventing fake vulnerabilities, tools, attack techniques, CVEs, or remediation steps. This is important in cybersecurity because a confident but false answer can lead to incorrect technical decisions.

### 7.2 Security Context Awareness

This criterion measures whether the model understands the professional cybersecurity context of the question. A strong model should distinguish between defensive analysis, authorized testing, and unsafe real-world misuse.

### 7.3 Code and Command Usability

This criterion measures whether the model provides commands, scripts, filters, and payloads that are syntactically correct and practically usable. In cybersecurity tasks, a response that sounds correct but contains broken commands is not reliable.

## 8. Comparative Analysis

### 8.1 Model size

Larger models generally performed better, but size was not the only factor. Mistral-Nemo-Instruct-2407 was the strongest overall model, but smaller models such as Qwen2.5-3B-Instruct and Phi-3.5-mini-instruct were still competitive.

TinyLlama showed that very small models are not reliable enough for this kind of cybersecurity evaluation.

### 8.2 General-purpose vs cybersecurity-specific models

The cybersecurity-focused models did not automatically outperform general-purpose or coder models. WhiteRabbitNeo was useful and competitive, but Lily-Cybersecurity-7B-v0.2 had weak hallucination-trap performance. This suggests that a cybersecurity label on Hugging Face is not enough to judge quality.

### 8.3 Coder models

Qwen2.5-Coder-7B-Instruct was one of the strongest practical models. It performed well on code review traps and command-generation tasks. However, it still failed several hallucination traps, so coder specialization improves practical output but does not solve factual reliability.

### 8.4 Hallucination behavior

Hallucination resistance was the weakest area across many models. Several otherwise strong models fabricated answers for fake CVEs or fictional attack names. This is important because cybersecurity work often depends on exact vulnerability identifiers and precise tool behavior.

### 8.5 Hardware practicality

Mistral-Nemo produced the best results, but it is heavier to run. For limited hardware, Qwen2.5-3B-Instruct and Phi-3.5-mini-instruct are better practical options. For code review and scripting on stronger hardware, Qwen2.5-Coder-7B-Instruct is a strong choice.

## 9. Limitations

The evaluation uses an LLM-as-a-judge approach. This makes scoring scalable, but the evaluator model may introduce bias or scoring inconsistencies. Selected answers, especially surprising high or low scores, should be manually reviewed.

All models were tested with GGUF Q4_K_M quantization where possible. This made local inference possible on consumer hardware, but results may differ from full-precision versions.

All models were tested with a fixed context length of 4096 tokens. Some models support larger native context windows, but long-context performance was not the focus of this project. Since each evaluation prompt contained a single cybersecurity question, 4096 tokens was sufficient for this benchmark.

Hardware constraints also affected the evaluation. Larger models required more VRAM/RAM and longer inference time. Practical usability was considered together with answer quality.

Temperature experiments are still required unless completed separately. The current uploaded results only show the baseline temperature = 0 evaluation.

## 10. Conclusion and Recommendation

Based on the baseline evaluation, the best overall model was Mistral-Nemo-Instruct-2407. It had the highest overall score and strongest practical subset score, making it the best choice when hardware resources are available.

For code review and practical cybersecurity scripting, Qwen2.5-Coder-7B-Instruct was one of the strongest choices. It performed well on code review traps and practical command-generation questions.

For lower-resource hardware, Qwen2.5-3B-Instruct and Phi-3.5-mini-instruct were the best compromises. They were much smaller than the 7B–12B models but still performed competitively.

Cybersecurity-focused models were useful for comparison, but they did not clearly outperform the strongest general-purpose and coder models. The evaluation suggests that model quality must be measured by accuracy, practical usefulness, and hallucination resistance rather than by the model name or category.

All tested models still require manual verification for high-risk cybersecurity work, especially when dealing with CVEs, exploit details, unfamiliar attack names, and exact command syntax.
