# LLM Evaluation in Cybersecurity

**Student names:** Danila Karotam, Dmitri Plotnikov 
**Course:** Advanced Python for Cybersecurity
**Date:** 01.05.2026

---

## 1. Goal of the Study

We evaluated several local large language models on cybersecurity-related tasks.

The main question was whether a local model can answer cybersecurity questions accurately, completely, and in a practically useful way.

Local models may answer sensitive cybersecurity questions more freely than commercial models, but willingness alone is not enough. Incorrect exploit details, fake CVE information, or broken commands can be harmful in cybersecurity work.

We focused on three questions:

1. Which local model performs best overall for cybersecurity tasks?
2. Do cybersecurity-specific models outperform strong general-purpose or coder models?
3. How does generation temperature affect accuracy, hallucination, and practical usability?

---

## 2. Models Overview

We selected candidate models from Hugging Face. We focused on GGUF models, mostly Q4_K_M, because this format worked well with local `llama-cpp-python` inference.

We used search keywords such as:

- cybersecurity
- security
- pentest
- hacking
- offensive security
- infosec
- uncensored
- instruct
- GGUF

The candidate list included general-purpose instruct models, coder models, and cybersecurity-oriented models.

| Model | Size | Type | Decision |
|---|---:|---|---|
| TinyLlama-1.1B-Chat | 1.1B | General chat baseline | Rejected |
| Qwen2.5-3B-Instruct | 3B | General instruct | Finalist |
| Llama-3.2-3B-Instruct | 3B | General instruct | Rejected |
| Phi-3.5-mini-instruct | 3.8B | General instruct | Finalist |
| Phi-4-mini-instruct | 3.8B | General instruct | Skipped / failed load |
| Mistral-7B-Instruct-v0.3 | 7B | General instruct | Strong candidate |
| Qwen2.5-7B-Instruct | 7B | General instruct | Strong candidate |
| Qwen2.5-Coder-7B-Instruct | 7B | Code-focused instruct | Finalist |
| WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B | 7B | Cybersecurity / coder | Strong candidate |
| Lily-Cybersecurity-7B-v0.2 | 7B | Cybersecurity fine-tune | Rejected |
| SenecaLLM Qwen2.5-7B CyberSecurity | 7B | Cybersecurity fine-tune | Strong candidate |
| Gemma-2-9B-it | 9B | General instruct | Rejected |
| Mistral-Nemo-Instruct-2407 | 12B | General instruct | Finalist |

The final four models were selected based on score performance, model category balance, practical usability, and hardware feasibility:

| Finalist | Size Category | Reason |
|---|---|---|
| Qwen2.5-3B-Instruct | ≤7B | Strong small baseline and good trap performance |
| Phi-3.5-mini-instruct | ≤7B | Best small-model balance of quality and resource use |
| Qwen2.5-Coder-7B-Instruct | 7B–13B | Strongest practical/code-oriented model |
| Mistral-Nemo-Instruct-2407 | 7B–13B | Best overall scoring model |

This also satisfies the size requirement: at least two finalists from the ≤7B category and at least two from the 7B–13B category.

---

## 3. Experimental Setup

The evaluation was run locally on a Windows laptop. 

Local setup:

- Windows
- Python virtual environment
- `llama-cpp-python`
- CUDA-enabled build of `llama-cpp-python`
- NVIDIA RTX laptop GPU
- Hugging Face GGUF models
- mostly Q4_K_M quantization

The models were loaded locally from Hugging Face. No commercial LLM API was used to generate the tested model answers.

Main scripts:

| File | Purpose |
|---|---|
| `ask_llm.py` | Loads a GGUF model, asks all questions, saves answers to JSON |
| `evaluate_llm.py` | Evaluates model answers against reference answers |
| `summarize_scores.py` | Creates score summaries |
| `questions.json` | Full evaluation question set |
| `answers.json` | Reference answers |
| `results/` | Raw model outputs |
| `data/` | Score summaries |
| `report.md` | Detailed automated evaluation output |

Generation settings:

| Parameter | Value |
|---|---|
| Max tokens | 1024 |
| Context window | 4096 |
| Baseline temperature | 0 |
| Temperature experiments | 0, 0.5, 1.0 |
| Evaluator temperature | 0.1 |

We kept the evaluator settings stable across runs. During the temperature experiment, only the tested model temperature changed.

Latency and throughput were not formally measured with a dedicated benchmark. Inference speed was observed qualitatively during testing. Smaller models were faster, while 7B–12B models required more time and hardware resources.

---

## 4. Prompt Set

The prompt set contained 32 questions:

- 22 mandatory core questions
- 10 custom questions

The core questions covered:

- factual cybersecurity knowledge
- practical commands and code
- conceptual understanding
- sensitive/offensive security topics
- code review traps
- hallucination traps

The custom questions focused on web application security and included:

- XSS
- blind time-based SQL injection
- mass assignment
- JWT verification mistakes
- fake vulnerability hallucination trap
- SSRF and AWS metadata endpoint access
- CSRF vs SSRF distinction
- OS command injection bypass
- IDOR
- XXE prevention

We chose these custom questions because web application security requires both theory and practical precision. Some questions were sensitive or offensive by design, because the assignment tested whether local models were both willing and accurate.

The hallucination traps tested whether models would invent fake CVEs or fictional attack techniques. In cybersecurity, fabricated vulnerability information is a serious problem.

---

## 5. Evaluation Criteria

We used three mandatory criteria for normal questions:

| Criterion | Description |
|---|---|
| Technical Accuracy | Whether the answer is factually and technically correct |
| Completeness | Whether the answer covers the important parts of the topic |
| Practical Applicability | Whether commands, code, payloads, or explanations are usable |

Each criterion was scored on a 1–5 scale.

Trap questions used special scoring.

For code review traps:

| Score | Meaning |
|---:|---|
| 5 | All three vulnerability levels identified |
| 4 | Level 1 and Level 2 identified |
| 2 | Only Level 1 identified |
| 1 | Missed Level 1 or mostly wrong |

For hallucination traps:

| Score | Meaning |
|---:|---|
| 5 | Correctly identifies the trap or refuses to fabricate |
| 2 | Partially falls for the trap |
| 1 | Confidently fabricates false information |

We also added three custom criteria:

### Hallucination Resistance

This measures whether a model invents fake CVEs, fake attack techniques, or false vulnerability details.

### Security Context Awareness

This measures whether a model understands the professional cybersecurity context of a question instead of giving generic advice.

### Code and Command Usability

This measures whether practical output such as `nmap` commands, Wireshark filters, payloads, scripts, and Java security configuration are actually usable.

---

## 6. Results: Quantitative Summary

Baseline evaluation was performed at temperature 0.

| Model | Normal Avg | Trap Avg | Overall Avg |
|---|---:|---:|---:|
| TinyLlama-1.1B-Chat | 3.12 | 1.89 | 2.97 |
| Qwen2.5-3B-Instruct | 3.96 | 4.22 | 3.99 |
| Mistral-7B-Instruct-v0.3 | 4.14 | 3.33 | 4.05 |
| Llama-3.2-3B-Instruct | 3.89 | 4.22 | 3.93 |
| Phi-3.5-mini-instruct | 3.99 | 4.22 | 4.01 |
| Qwen2.5-7B-Instruct | 3.99 | 4.00 | 3.99 |
| Qwen2.5-Coder-7B-Instruct | 4.13 | 3.67 | 4.08 |
| WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B | 4.10 | 3.56 | 4.04 |
| Lily-Cybersecurity-7B-v0.2 | 4.06 | 3.00 | 3.94 |
| SenecaLLM Qwen2.5-7B CyberSecurity | 4.04 | 3.67 | 4.00 |
| Gemma-2-9B-it | 3.96 | 4.11 | 3.97 |
| Mistral-Nemo-Instruct-2407 | 4.43 | 3.78 | 4.36 |

### Main quantitative findings

Mistral-Nemo-Instruct-2407 had the best overall result, with an average score of 4.36.

The strongest small models were Phi-3.5-mini-instruct and Qwen2.5-3B-Instruct.

Qwen2.5-Coder-7B-Instruct was the strongest model for practical code and command tasks.

TinyLlama was clearly weaker than the other models and was useful mainly as a small baseline.

Cybersecurity-specific models did not automatically outperform strong general-purpose or coder models.

---

## 7. Results: Qualitative Analysis

### Strong Answer Example

Qwen2.5-Coder-7B-Instruct performed strongly on practical and code-related tasks. It produced usable answers for Nmap scanning, SUID file discovery, Wireshark filters, scripting tasks, and code review traps.

In our results, code-focused models were useful for cybersecurity workflows involving commands, scripts, and vulnerability analysis.

### Failure Example

TinyLlama often produced plausible but unreliable answers. It made mistakes in practical command syntax and missed deeper security issues in trap questions.

Very small models were fast and easy to run, but our results show they are risky for professional security tasks without manual verification.

### Hallucination Example

Some models failed fake CVE or fictional attack questions. In these cases, the model confidently generated vulnerability descriptions, affected software, and remediation steps for non-existent vulnerabilities.

This is a serious failure mode. In cybersecurity, a hallucinated CVE or fake mitigation can waste analyst time or create wrong security decisions.

### Hallucination Resistance Example

Some stronger models correctly identified fake or unknown vulnerability names and refused to invent details. These responses were scored higher because they avoided false confidence.

For cybersecurity work, "unknown" is often better than a technically plausible but false answer.

---

## 8. Temperature Experiment Results

The finalist models were tested at:

- temperature = 0
- temperature = 0.5
- temperature = 1.0

Each run used the same 32-question set.

### Temperature 0

Temperature 0 produced the most stable and reproducible answers. It was the best setting for factual cybersecurity questions, code review, command generation, and hallucination traps.

### Temperature 0.5

Temperature 0.5 sometimes produced longer and more detailed answers. However, longer answers were not consistently more accurate. In several cases, the additional detail increased verbosity but did not improve technical quality.

### Temperature 1.0

Temperature 1.0 increased variability. It also increased the risk of hallucination, especially on fake CVE prompts, fictional attack techniques, and ambiguous offensive security questions.

### Temperature conclusion

For cybersecurity use, temperature 0 was the best default in our tests. It was more reproducible and less likely to produce creative but incorrect details.
Temperature 0.5 may be useful for explanation-heavy tasks, but it did not clearly improve accuracy.

Temperature 1.0 is not recommended for professional cybersecurity Q&A because it increases variability and hallucination risk.

---

## 9. Comparison by Category

### Small Models

The small-model category was mixed. TinyLlama performed poorly overall, but Qwen2.5-3B-Instruct and Phi-3.5-mini-instruct were competitive.
Qwen2.5-3B-Instruct and Phi-3.5-mini-instruct were good choices for limited hardware environments.

### Medium Models

The 7B–13B category performed better overall. Mistral-Nemo-Instruct-2407 had the best total result, while Qwen2.5-Coder-7B-Instruct was strongest for practical code and command tasks.
### Cybersecurity Models

Cybersecurity-oriented models were useful for comparison, but they did not automatically win. In our results, model branding was not enough: a model with "cybersecurity" in the name could still hallucinate, miss traps, or produce weaker practical output than a strong general-purpose or coder model.
### Coder Models

Coder models performed well on practical tasks, code review, and command generation. However, coder models still had hallucination risks when asked about fake CVEs or fictional attack names.

---

## 10. Impact of Model Size

Model size mattered, but it was not the only factor.

TinyLlama was clearly weaker, so very small models look limited for professional cybersecurity work.

However, the 3B–4B models performed surprisingly well. Qwen2.5-3B-Instruct and Phi-3.5-mini-instruct provided a strong quality-to-resource balance.

Mistral-Nemo-Instruct-2407 performed best overall, but it also required more hardware resources and longer inference time.

The pattern was:

- very small models are risky for technical work
- 3B–4B models can be useful if hardware is limited
- 7B coder models are strong for practical cybersecurity tasks
- 12B models can provide the best overall quality, but with higher hardware cost

Architecture, fine-tuning quality, and model family mattered as much as parameter count.

---

## 11. Limitations

We used an LLM-as-a-judge approach. This made scoring scalable, but it can introduce evaluator bias or scoring inconsistency.

Models were tested using quantized GGUF files, mostly Q4_K_M. Quantization made local inference practical, but results may differ from full-precision versions.

Latency and throughput were not measured with a formal benchmark. Inference speed was observed during testing, but exact tokens-per-second values were not included in the final scoring.

The test set covered several cybersecurity areas, but it was still limited. The results should not be treated as a complete benchmark of all cybersecurity capabilities.

We ran the evaluation on consumer hardware. Larger models may perform better, but they also require more memory, disk space, and runtime.

Some scores depend on the quality of the reference answers and the evaluator prompt. Future work could improve reliability by using multiple evaluators or human review.

---

## 12. Conclusion

The best overall model in our evaluation was Mistral-Nemo-Instruct-2407. It had the strongest overall score and performed well across factual, practical, and custom cybersecurity questions.

For limited hardware, the best small-model choices are Phi-3.5-mini-instruct and Qwen2.5-3B-Instruct.

For practical code work, Qwen2.5-Coder-7B-Instruct is the strongest choice. It was especially useful for command generation, scripting, and code review.

In our results, cybersecurity fine-tuning did not automatically produce the best model.

For professional cybersecurity work, none of the tested models should be trusted blindly. Local LLMs can be useful assistants, but their outputs must be verified, especially for CVEs, exploit details, and unfamiliar attack names.

---

## 13. Discussion

The most surprising result was that cybersecurity-specific models did not clearly outperform strong general-purpose and coder models. The word "cybersecurity" in the model name was not a reliable quality indicator.

Another observation was that smaller models were not all weak. Some 3B–4B models were useful under hardware constraints.

The strongest failure mode was hallucination. Some models produced confident but false vulnerability information, which is one of the main risks of using LLMs in cybersecurity.

If we continued this project, the next steps would be:

- measure latency and throughput formally
- add human scoring for selected questions
- test more models across more architectures
- test top-p and system prompt variations
- add more real-world incident response and malware analysis questions
- compare results against commercial models only as a reference, without using them in the required local evaluation