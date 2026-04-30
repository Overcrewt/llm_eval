# Screening Log

The screening phase was used to compare candidate local LLMs before selecting finalists for deeper analysis. The screening focused on factual knowledge, practical command quality, code-review traps, hallucination traps, and custom web-security tasks. The score values below come from the automated evaluator output in `report.md` and the summary table in `data/model_score_summary.csv`.

## TinyLlama-1.1B-Chat-v1.0

Status: Tested  
Size category: ≤7B  
Type: General-purpose chat baseline  

Score summary:
- Normal score average: 3.12
- Trap score average: 1.89
- Overall average: 2.97
- Factual subset average: 3.33
- Practical subset average: 2.50
- Code-review trap average: 2.60
- Hallucination trap average: 1.00

Observations:
- Factual knowledge: Medium to strong. The model's factual and conceptual answers were usually in the 3-point range.
- Practical command quality: Medium. This was judged from nmap, Linux, Wireshark, scripting, web-security payload, SSRF, command-injection, and XXE tasks.
- Code review trap performance: Medium. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Medium overall, based mainly on web-application security tasks.

Decision: Rejected

Reason:
Small baseline only; weak practical answers and very poor hallucination-trap performance.

---

## Qwen2.5-3B-Instruct

Status: Tested  
Size category: ≤7B  
Type: General-purpose  

Score summary:
- Normal score average: 3.96
- Trap score average: 4.22
- Overall average: 3.99
- Factual subset average: 4.12
- Practical subset average: 3.83
- Code-review trap average: 4.80
- Hallucination trap average: 3.50

Observations:
- Factual knowledge: Strong. The model's factual and conceptual answers were usually in the 4-point range.
- Practical command quality: Medium to strong. This was judged from nmap, Linux, Wireshark, scripting, web-security payload, SSRF, command-injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Medium to strong. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Medium to strong overall, based mainly on web-application security tasks.

Decision: Finalist

Reason:
Strong small model with good trap performance and good quality-to-resource ratio.

---

## Mistral-7B-Instruct-v0.3

Status: Tested  
Size category: 7B–13B  
Type: General-purpose  

Score summary:
- Normal score average: 4.14
- Trap score average: 3.33
- Overall average: 4.05
- Factual subset average: 4.12
- Practical subset average: 4.38
- Code-review trap average: 4.80
- Hallucination trap average: 1.50

Observations:
- Factual knowledge: Strong. The model's factual and conceptual answers were usually in the 4-point range.
- Practical command quality: Strong. This was judged from nmap, Linux, Wireshark, scripting, web-security payload, SSRF, command-injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Strong overall, based mainly on web-application security tasks.

Decision: Finalist

Reason:
Strong general-purpose 7B baseline with high normal/practical scores, but weak hallucination resistance.

---

## Llama-3.2-3B-Instruct

Status: Tested  
Size category: ≤7B  
Type: General-purpose  

Score summary:
- Normal score average: 3.89
- Trap score average: 4.22
- Overall average: 3.93
- Factual subset average: 4.08
- Practical subset average: 3.95
- Code-review trap average: 5.00
- Hallucination trap average: 3.25

Observations:
- Factual knowledge: Strong. The model's factual and conceptual answers were usually in the 4-point range.
- Practical command quality: Medium to strong. This was judged from nmap, Linux, Wireshark, scripting, web-security payload, SSRF, command-injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Medium. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Medium to strong overall, based mainly on web-application security tasks.

Decision: Rejected / backup

Reason:
Good trap performance, but lower overall and practical score than Qwen2.5-3B and Phi-3.5-mini.

---

## Phi-3.5-mini-instruct

Status: Tested  
Size category: ≤7B  
Type: General-purpose  

Score summary:
- Normal score average: 3.99
- Trap score average: 4.22
- Overall average: 4.01
- Factual subset average: 4.12
- Practical subset average: 3.79
- Code-review trap average: 5.00
- Hallucination trap average: 3.25

Observations:
- Factual knowledge: Strong. The model's factual and conceptual answers were usually in the 4-point range.
- Practical command quality: Medium to strong. This was judged from nmap, Linux, Wireshark, scripting, web-security payload, SSRF, command-injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Medium. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Medium to strong overall, based mainly on web-application security tasks.

Decision: Finalist

Reason:
Best small-model overall score and strong trap performance.

---

## PHI-4-MINI-INSTRUCT

Status: Skipped  
Size category: ≤7B  
Type: General-purpose instruct model  

Score summary:
- Normal score average: N/A
- Trap score average: N/A
- Overall average: N/A

Observations:
- Factual knowledge: Not evaluated.
- Practical command quality: Not evaluated.
- Code review trap performance: Not evaluated.
- Hallucination trap performance: Not evaluated.
- Custom cybersecurity task performance: Not evaluated.

Decision: Skipped

Reason:
The model was downloaded successfully but failed to load with the current `llama-cpp-python` CUDA backend. It was excluded from finalist selection because no valid output was produced.

---

## Qwen2.5-7B-Instruct

Status: Tested  
Size category: 7B–13B  
Type: General-purpose  

Score summary:
- Normal score average: 3.99
- Trap score average: 4.00
- Overall average: 3.99
- Factual subset average: 4.00
- Practical subset average: 3.79
- Code-review trap average: 5.00
- Hallucination trap average: 2.75

Observations:
- Factual knowledge: Strong. The model's factual and conceptual answers were usually in the 4-point range.
- Practical command quality: Medium to strong. This was judged from nmap, Linux, Wireshark, scripting, web-security payload, SSRF, command-injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Medium. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Medium to strong overall, based mainly on web-application security tasks.

Decision: Rejected / backup

Reason:
Good balanced result, but less distinctive than Qwen2.5-Coder and Mistral-Nemo.

---

## Qwen2.5-Coder-7B-Instruct

Status: Tested  
Size category: 7B–13B  
Type: Coder / instruct  

Score summary:
- Normal score average: 4.13
- Trap score average: 3.67
- Overall average: 4.08
- Factual subset average: 4.04
- Practical subset average: 4.54
- Code-review trap average: 5.00
- Hallucination trap average: 2.00

Observations:
- Factual knowledge: Strong. The model's factual and conceptual answers were usually in the 4-point range.
- Practical command quality: Very strong. This was judged from nmap, Linux, Wireshark, scripting, web-security payload, SSRF, command-injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Very strong overall, based mainly on web-application security tasks.

Decision: Finalist

Reason:
Best code/practical-oriented 7B choice; strong command and code review performance.

---

## WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B

Status: Tested  
Size category: 7B–13B  
Type: Coder / cybersecurity-oriented  

Score summary:
- Normal score average: 4.10
- Trap score average: 3.56
- Overall average: 4.04
- Factual subset average: 3.96
- Practical subset average: 4.17
- Code-review trap average: 4.80
- Hallucination trap average: 2.00

Observations:
- Factual knowledge: Medium to strong. The model's factual and conceptual answers were usually in the 4-point range.
- Practical command quality: Strong. This was judged from nmap, Linux, Wireshark, scripting, web-security payload, SSRF, command-injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Strong overall, based mainly on web-application security tasks.

Decision: Finalist

Reason:
Cybersecurity/coder model useful for comparing security-oriented fine-tunes against general models.

---

## Lily-Cybersecurity-7B-v0.2

Status: Tested  
Size category: 7B–13B  
Type: Cybersecurity fine-tune  

Score summary:
- Normal score average: 4.06
- Trap score average: 3.00
- Overall average: 3.94
- Factual subset average: 4.08
- Practical subset average: 4.17
- Code-review trap average: 4.60
- Hallucination trap average: 1.00

Observations:
- Factual knowledge: Strong. The model's factual and conceptual answers were usually in the 4-point range.
- Practical command quality: Strong. This was judged from nmap, Linux, Wireshark, scripting, web-security payload, SSRF, command-injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Strong overall, based mainly on web-application security tasks.

Decision: Rejected

Reason:
Good normal score but weak hallucination-trap average; did not outperform stronger general/coder models.

---

## SenecaLLM_x_Qwen2.5-7B-CyberSecurity

Status: Tested  
Size category: 7B–13B  
Type: Cybersecurity fine-tune  

Score summary:
- Normal score average: 4.04
- Trap score average: 3.67
- Overall average: 4.00
- Factual subset average: 4.00
- Practical subset average: 4.50
- Code-review trap average: 4.80
- Hallucination trap average: 2.25

Observations:
- Factual knowledge: Strong. The model's factual and conceptual answers were usually in the 4-point range.
- Practical command quality: Very strong. This was judged from nmap, Linux, Wireshark, scripting, web-security payload, SSRF, command-injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Very strong overall, based mainly on web-application security tasks.

Decision: Rejected / backup

Reason:
Good practical score, but slightly weaker overall and less distinctive than WhiteRabbitNeo and Qwen2.5-Coder.

---

## Gemma-2-9B-it

Status: Tested  
Size category: 7B–13B  
Type: General-purpose  

Score summary:
- Normal score average: 3.96
- Trap score average: 4.11
- Overall average: 3.97
- Factual subset average: 4.12
- Practical subset average: 3.75
- Code-review trap average: 5.00
- Hallucination trap average: 3.00

Observations:
- Factual knowledge: Strong. The model's factual and conceptual answers were usually in the 4-point range.
- Practical command quality: Medium to strong. This was judged from nmap, Linux, Wireshark, scripting, web-security payload, SSRF, command-injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Medium. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Medium to strong overall, based mainly on web-application security tasks.

Decision: Rejected / backup

Reason:
Good hallucination resistance compared with several 7B models, but lower practical score and less relevant to the security-model comparison.

---

## Mistral-Nemo-Instruct-2407

Status: Tested  
Size category: 7B–13B  
Type: General-purpose instruct  

Score summary:
- Normal score average: 4.43
- Trap score average: 3.78
- Overall average: 4.36
- Factual subset average: 4.29
- Practical subset average: 4.71
- Code-review trap average: 5.00
- Hallucination trap average: 2.25

Observations:
- Factual knowledge: Strong. The model's factual and conceptual answers were usually in the 4-point range.
- Practical command quality: Very strong. This was judged from nmap, Linux, Wireshark, scripting, web-security payload, SSRF, command-injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Very strong overall, based mainly on web-application security tasks.

Decision: Finalist

Reason:
Best overall model and strongest practical score, but heavier hardware requirements.

---

## Screening Summary

The screening showed that model size alone did not fully determine quality. TinyLlama was much weaker than the rest and was useful mainly as a low-resource baseline. Several small models, especially Qwen2.5-3B-Instruct and Phi-3.5-mini-instruct, performed competitively despite their lower parameter count.

The strongest overall model was Mistral-Nemo-Instruct-2407. The strongest code/practical candidate was Qwen2.5-Coder-7B-Instruct. The cybersecurity-focused models were useful for comparison, but the cybersecurity label did not automatically mean better accuracy or hallucination resistance. Lily-Cybersecurity-7B-v0.2, for example, had a good normal score but very weak hallucination-trap performance.

Selected finalists:
1. Qwen2.5-3B-Instruct
2. Phi-3.5-mini-instruct
3. Mistral-7B-Instruct-v0.3
4. Qwen2.5-Coder-7B-Instruct
5. WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B
6. Mistral-Nemo-Instruct-2407
