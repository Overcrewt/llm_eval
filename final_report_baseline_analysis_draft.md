# Cybersecurity LLM Evaluation Report

## 1. Introduction

This project evaluates local large language models for cybersecurity-related tasks. The goal is to compare models that can be run locally or in a self-hosted environment without using commercial APIs.

The core question is practical: a local model can be willing to answer cybersecurity questions, but willingness alone is not useful. A professional cybersecurity assistant must also be technically accurate, produce usable commands or code, and avoid fabricating vulnerabilities or attack techniques.

## 2. Methodology

The project followed three main phases.

First, candidate models were collected from Hugging Face. The selection focused on local GGUF models, preferably Q4_K_M quantization. The candidate list included general-purpose instruct/chat models, code-focused models, and cybersecurity-focused fine-tunes. A general-purpose baseline was included to test whether cybersecurity-specific fine-tuning provides a measurable advantage.

Second, models were screened using questions from several categories: factual knowledge, practical command generation, conceptual understanding, offensive/security-sensitive tasks, code-review traps, and hallucination traps. Weak models were rejected if they produced incoherent answers, failed many practical tasks, hallucinated on trap questions, or did not provide a useful comparison point.

Third, selected models were evaluated on the full 32-question set. The set contained 22 mandatory core questions and 10 custom questions focused on web application security. Raw answers were saved as JSON files and scored using an automated LLM-as-a-judge evaluator.

Baseline runs used:

- GGUF models
- mostly Q4_K_M quantization
- `llama-cpp-python`
- local RTX/CUDA acceleration
- context length: 4096 tokens
- tested-model temperature: 0

The evaluator model was kept fixed across evaluations with a low temperature setting. This makes scoring more consistent, although the LLM-as-a-judge approach still has limitations.

## 3. Reconnaissance Log

Candidate models were selected from Hugging Face using keywords such as `cybersecurity`, `security`, `pentest`, `hacking`, `offensive security`, `infosec`, `uncensored`, `instruct`, `coder`, and `GGUF`.

The candidate list included small models, 7B-class models, cybersecurity-focused models, and larger 9B–12B models. This made it possible to compare model size, architecture, specialization, and hardware cost.

| Model | Normal Avg | Trap Avg | Overall | Practical | Hallucination | Decision |
|---|---|---|---|---|---|---|
| Mistral-Nemo-Instruct-2407 | 4.43 | 3.78 | 4.36 | 4.71 | 2.25 | Finalist |
| Qwen2.5-Coder-7B-Instruct | 4.13 | 3.67 | 4.08 | 4.54 | 2.0 | Finalist |
| Mistral-7B-Instruct-v0.3 | 4.14 | 3.33 | 4.05 | 4.38 | 1.5 | Comparison / not finalist |
| WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B | 4.1 | 3.56 | 4.04 | 4.17 | 2.0 | Comparison / not finalist |
| Phi-3.5-mini-instruct | 3.99 | 4.22 | 4.01 | 3.79 | 3.25 | Finalist |
| SenecaLLM_x_Qwen2.5-7B-CyberSecurity | 4.04 | 3.67 | 4.0 | 4.5 | 2.25 | Comparison / not finalist |
| Qwen2.5-3B-Instruct | 3.96 | 4.22 | 3.99 | 3.83 | 3.5 | Finalist |
| Qwen2.5-7B-Instruct | 3.99 | 4.0 | 3.99 | 3.79 | 2.75 | Comparison / not finalist |
| Gemma-2-9B-it | 3.96 | 4.11 | 3.97 | 3.75 | 3.0 | Comparison / not finalist |
| Lily-Cybersecurity-7B-v0.2 | 4.06 | 3.0 | 3.94 | 4.17 | 1.0 | Rejected / not finalist |
| Llama-3.2-3B-Instruct | 3.89 | 4.22 | 3.93 | 3.95 | 3.25 | Comparison / not finalist |
| TinyLlama-1.1B-Chat-v1.0 | 3.12 | 1.89 | 2.97 | 2.5 | 1.0 | Rejected baseline |


`Phi-4-mini-instruct` was attempted but skipped because it failed to load with the current CUDA backend.

## 4. Screening Results

The screening phase showed clear differences between models.

TinyLlama was useful only as a weak baseline. It was small and fast, but its practical command quality and hallucination resistance were too weak for professional cybersecurity use.

Qwen2.5-3B-Instruct and Phi-3.5-mini-instruct were the strongest small models. Both gave much better results than TinyLlama while still having lower hardware requirements than 7B–12B models.

Mistral-7B-Instruct-v0.3 was a strong general-purpose 7B baseline, but it had weaker hallucination resistance than the selected small finalists.

Qwen2.5-Coder-7B-Instruct was one of the strongest models for practical command generation and code-review tasks. It was selected as a finalist because code and command usability are central to cybersecurity workflows.

Mistral-Nemo-Instruct-2407 had the highest overall baseline score. It was selected as the strongest larger general-purpose model.

Cybersecurity-focused models such as WhiteRabbitNeo, Lily, and Seneca were useful for comparison, but they did not automatically outperform the strongest general-purpose or coder models. This supports the idea that model names and domain labels are not enough; models must be tested.

Finalists selected:

| Model | Size category | Reason |
|---|---|---|
| Qwen2.5-3B-Instruct | ≤7B | Strong small model and good trap performance |
| Phi-3.5-mini-instruct | ≤7B | Best small-model overall score and stable behavior |
| Qwen2.5-Coder-7B-Instruct | 7B–13B | Strongest practical/code-focused finalist |
| Mistral-Nemo-Instruct-2407 | 7B–13B | Best overall baseline score |

This satisfies the required minimum of four finalists with at least two models from each mandatory size category.

## 5. Full Evaluation Results

The full baseline evaluation showed three main patterns.

First, larger models generally performed better, but not perfectly. Mistral-Nemo had the best overall score, but it still had weaknesses in hallucination traps.

Second, coder models performed especially well on code review and practical command tasks. Qwen2.5-Coder-7B was strong on nmap, SUID search, Wireshark filters, code review, and several custom web-security questions.

Third, hallucination resistance remained a problem across nearly all models. Even strong models sometimes gave plausible-sounding answers for fake CVEs or fictional vulnerability names.

The strongest baseline models were:

| Category | Best model | Reason |
|---|---|---|
| Best overall | Mistral-Nemo-Instruct-2407 | Highest overall score |
| Best small model | Phi-3.5-mini-instruct / Qwen2.5-3B-Instruct | Strong results with lower resource use |
| Best practical/code model | Qwen2.5-Coder-7B-Instruct | Strong command and code-review performance |
| Best weak baseline | TinyLlama-1.1B-Chat-v1.0 | Useful only as a low-resource baseline |
| Best cybersecurity comparison | WhiteRabbitNeo / Seneca | Useful comparison, but not clearly better than general/coder models |

## 6. Parameter Experiments

The four finalists were tested at `temperature = 0`, `temperature = 0.5`, and `temperature = 1.0`.

| Model | Temp | Overall | Trap Avg | Hallucination | Practical | Code Review |
|---|---|---|---|---|---|---|
| Qwen2.5-3B-Instruct | 0 | 3.99 | 4.22 | 3.5 | 3.83 | 4.8 |
| Qwen2.5-3B-Instruct | 0.5 | 3.94 | 4.56 | 4.25 | 3.71 | 4.8 |
| Qwen2.5-3B-Instruct | 1.0 | 4.07 | 3.67 | 2.0 | 4.19 | 5.0 |
| Phi-3.5-mini-instruct | 0 | 4.01 | 4.22 | 3.25 | 3.79 | 5.0 |
| Phi-3.5-mini-instruct | 0.5 | 4.05 | 4.22 | 3.25 | 3.92 | 5.0 |
| Phi-3.5-mini-instruct | 1.0 | 3.96 | 4.0 | 3.0 | 4.0 | 4.8 |
| Qwen2.5-Coder-7B-Instruct | 0 | 4.08 | 3.67 | 2.0 | 4.54 | 5.0 |
| Qwen2.5-Coder-7B-Instruct | 0.5 | 3.96 | 4.0 | 3.0 | 4.0 | 4.8 |
| Qwen2.5-Coder-7B-Instruct | 1.0 | 4.19 | 4.11 | 3.0 | 4.5 | 5.0 |
| Mistral-Nemo-Instruct-2407 | 0 | 4.36 | 3.78 | 2.25 | 4.71 | 5.0 |
| Mistral-Nemo-Instruct-2407 | 0.5 | 4.32 | 3.56 | 1.75 | 4.62 | 5.0 |
| Mistral-Nemo-Instruct-2407 | 1.0 | 4.23 | 3.33 | 1.25 | 4.5 | 5.0 |


Main findings:

- `temperature = 0` was the safest setting for reproducible cybersecurity answers.
- `temperature = 0.5` sometimes improved detail or trap behavior, but the effect was not consistent.
- `temperature = 1.0` increased variability and could reduce hallucination resistance.
- Mistral-Nemo showed the clearest degradation as temperature increased.
- Phi-3.5-mini was relatively stable across temperatures.
- Qwen2.5-Coder remained strong on code and practical questions, but high-temperature answers still require manual verification.

For professional cybersecurity use, lower temperature is preferable. Higher temperature may be useful for brainstorming, but not for final technical guidance.

## 7. Custom Criteria

In addition to the mandatory scoring criteria, three custom criteria were used.

### 7.1 Hallucination resistance

This criterion measures whether the model avoids inventing fake vulnerabilities, CVEs, tools, or attack techniques. It is important because a confident but false cybersecurity answer can lead to wrong technical decisions.

### 7.2 Security context awareness

This criterion measures whether the model understands the context of authorized security testing, defensive analysis, and risky offensive use. A useful cybersecurity assistant should not only provide technical output but also frame it in a professional context.

### 7.3 Code and command usability

This criterion measures whether commands, scripts, filters, and payloads are syntactically correct and practically usable. In cybersecurity, a command that sounds correct but contains wrong flags or malformed syntax can waste time or mislead the analyst.

## 8. Comparative Analysis

### Model size

Model size helped, but it was not the only factor. Mistral-Nemo was the strongest overall model, but smaller models such as Phi-3.5-mini and Qwen2.5-3B performed surprisingly well.

### General-purpose vs cybersecurity-focused models

Cybersecurity-focused models did not automatically win. WhiteRabbitNeo, Lily, and Seneca were useful, but the strongest overall and practical results came from Mistral-Nemo and Qwen2.5-Coder. This suggests that strong general-purpose or coder models can outperform weaker domain fine-tunes.

### Code-focused models

Qwen2.5-Coder-7B was especially useful for practical cybersecurity work. It handled code-review traps and command-generation tasks well. Its main weakness was still hallucination risk on fictional vulnerability prompts.

### Hallucination behavior

Hallucination remained the most important risk. Several models could correctly explain real security concepts but still fabricate details about fake CVEs or fictional attacks. This means local LLMs should not be trusted blindly for vulnerability identification.

### Hardware practicality

Small models were easier to run and still useful. Qwen2.5-3B and Phi-3.5-mini were the best choices under hardware constraints. Larger models gave stronger results, but required more VRAM/RAM and time.

## 9. Limitations

The evaluation uses an LLM-as-a-judge approach. This makes scoring scalable, but the evaluator model may introduce bias or scoring inconsistencies. Selected answers, especially surprising high or low scores, should be manually reviewed.

All models were tested with GGUF Q4_K_M quantization where available. This made local inference practical on consumer hardware, but results may differ from full-precision versions.

All models were tested with a fixed context length of 4096 tokens. Some models support larger native context windows, but long-context performance was not the focus of this project. Since each prompt contained one question, 4096 tokens was sufficient for this benchmark.

The initial script version used a fallback completion path with a different low temperature. The evaluated models were mainly instruct/chat GGUF models, so the main chat-completion path was used. Later runs standardized the temperature through one shared variable.

The test set is limited to 32 questions. It covers many cybersecurity categories, but it cannot represent all professional cybersecurity tasks.

## 10. Conclusion and Recommendation

The best overall model was `Mistral-Nemo-Instruct-2407`. It had the highest baseline score and strong performance on factual, practical, and custom cybersecurity questions. Its main downside is higher hardware cost.

The best code and practical security model was `Qwen2.5-Coder-7B-Instruct`. It was strong on code review, command generation, and scripting tasks. It is a good choice when the main use case is practical technical work.

The best small-model choices were `Phi-3.5-mini-instruct` and `Qwen2.5-3B-Instruct`. They gave strong results for their size and are better options for limited hardware.

Cybersecurity-focused fine-tunes were useful for comparison, but they did not automatically outperform the strongest general-purpose and coder models. The evaluation supports the conclusion that a cybersecurity model must be judged by accuracy, practical usability, and hallucination resistance rather than by its name or willingness to answer.

Final recommendation:

- Use `Mistral-Nemo-Instruct-2407` when quality matters most and hardware is available.
- Use `Qwen2.5-Coder-7B-Instruct` for code review and practical command/script tasks.
- Use `Phi-3.5-mini-instruct` or `Qwen2.5-3B-Instruct` when hardware resources are limited.
- Manually verify all CVE-related, exploit-related, and unfamiliar attack-name answers.
