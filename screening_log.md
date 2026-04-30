# Screening Log

The screening phase was used to compare candidate local LLMs before selecting finalists for temperature experiments and final analysis. The screening focused on factual knowledge, practical command quality, code-review traps, hallucination traps, and custom web-security tasks.

Scores come from the automated evaluator output in `report.md`. The decision is not based only on the overall average. It also considers model category, hardware cost, code-review usefulness, hallucination resistance, and whether the model adds a useful comparison point.

## Finalist selection

Finalists selected for parameter experiments:

1. `Qwen2.5-3B-Instruct`
2. `Phi-3.5-mini-instruct`
3. `Qwen2.5-Coder-7B-Instruct`
4. `Mistral-Nemo-Instruct-2407`

This satisfies the requirement of at least four finalists with at least two models from the `≤7B` category and at least two models from the `7B–13B` category.

## Gemma-2-9B-it

Status: Tested  
Size category: 7B–13B  
Type: General-purpose instruct model  

Score summary:
- Normal score average: 3.96
- Trap score average: 4.11
- Overall average: 3.97
- Factual subset average: 4.14
- Practical subset average: 3.75
- Code-review trap average: 5.0
- Hallucination trap average: 3.0

Observations:
- Factual knowledge: Strong. This was judged from TCP, encryption, CVSS, IDS/IPS, TLS 1.3, threat terminology, and pentest methodology questions.
- Practical command quality: Medium to strong. This was judged from nmap, SUID search, Wireshark filters, scripting, web-security payloads, command injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Medium. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Medium to strong. This covered XSS, SQL injection, mass assignment, SSRF, CSRF/SSRF, command injection, IDOR, and XXE questions.

Decision: Comparison / not finalist

Reason:
Good general-purpose model, but not selected because it did not outperform Mistral-Nemo and did not add a unique capability.

---

## Lily-Cybersecurity-7B-v0.2

Status: Tested  
Size category: 7B–13B  
Type: Cybersecurity fine-tune  

Score summary:
- Normal score average: 4.06
- Trap score average: 3.0
- Overall average: 3.94
- Factual subset average: 4.1
- Practical subset average: 4.17
- Code-review trap average: 4.6
- Hallucination trap average: 1.0

Observations:
- Factual knowledge: Strong. This was judged from TCP, encryption, CVSS, IDS/IPS, TLS 1.3, threat terminology, and pentest methodology questions.
- Practical command quality: Strong. This was judged from nmap, SUID search, Wireshark filters, scripting, web-security payloads, command injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Medium to strong. This covered XSS, SQL injection, mass assignment, SSRF, CSRF/SSRF, command injection, IDOR, and XXE questions.

Decision: Rejected / not finalist

Reason:
Not selected because hallucination-trap performance was weak despite reasonable normal scores.

---

## Llama-3.2-3B-Instruct

Status: Tested  
Size category: ≤7B  
Type: General-purpose instruct model  

Score summary:
- Normal score average: 3.89
- Trap score average: 4.22
- Overall average: 3.93
- Factual subset average: 4.1
- Practical subset average: 3.95
- Code-review trap average: 5.0
- Hallucination trap average: 3.25

Observations:
- Factual knowledge: Strong. This was judged from TCP, encryption, CVSS, IDS/IPS, TLS 1.3, threat terminology, and pentest methodology questions.
- Practical command quality: Medium to strong. This was judged from nmap, SUID search, Wireshark filters, scripting, web-security payloads, command injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Medium. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Medium to strong. This covered XSS, SQL injection, mass assignment, SSRF, CSRF/SSRF, command injection, IDOR, and XXE questions.

Decision: Comparison / not finalist

Reason:
Good small model, but slightly weaker than Qwen2.5-3B and Phi-3.5-mini for finalist selection.

---

## Mistral-7B-Instruct-v0.3

Status: Tested  
Size category: 7B–13B  
Type: General-purpose instruct model  

Score summary:
- Normal score average: 4.14
- Trap score average: 3.33
- Overall average: 4.05
- Factual subset average: 4.14
- Practical subset average: 4.38
- Code-review trap average: 4.8
- Hallucination trap average: 1.5

Observations:
- Factual knowledge: Strong. This was judged from TCP, encryption, CVSS, IDS/IPS, TLS 1.3, threat terminology, and pentest methodology questions.
- Practical command quality: Strong. This was judged from nmap, SUID search, Wireshark filters, scripting, web-security payloads, command injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Medium to strong. This covered XSS, SQL injection, mass assignment, SSRF, CSRF/SSRF, command injection, IDOR, and XXE questions.

Decision: Comparison / not finalist

Reason:
Strong general-purpose baseline, but not selected because Mistral-Nemo and Qwen2.5-Coder gave more useful finalist coverage.

---

## Mistral-Nemo-Instruct-2407

Status: Tested  
Size category: 7B–13B  
Type: General-purpose instruct model  

Score summary:
- Normal score average: 4.43
- Trap score average: 3.78
- Overall average: 4.36
- Factual subset average: 4.33
- Practical subset average: 4.71
- Code-review trap average: 5.0
- Hallucination trap average: 2.25

Observations:
- Factual knowledge: Strong. This was judged from TCP, encryption, CVSS, IDS/IPS, TLS 1.3, threat terminology, and pentest methodology questions.
- Practical command quality: Very strong. This was judged from nmap, SUID search, Wireshark filters, scripting, web-security payloads, command injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak to medium. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Strong. This covered XSS, SQL injection, mass assignment, SSRF, CSRF/SSRF, command injection, IDOR, and XXE questions.

Decision: Finalist

Reason:
Selected as a finalist because it had the best overall baseline score.

---

## Phi-3.5-mini-instruct

Status: Tested  
Size category: ≤7B  
Type: General-purpose instruct model  

Score summary:
- Normal score average: 3.99
- Trap score average: 4.22
- Overall average: 4.01
- Factual subset average: 4.14
- Practical subset average: 3.79
- Code-review trap average: 5.0
- Hallucination trap average: 3.25

Observations:
- Factual knowledge: Strong. This was judged from TCP, encryption, CVSS, IDS/IPS, TLS 1.3, threat terminology, and pentest methodology questions.
- Practical command quality: Medium to strong. This was judged from nmap, SUID search, Wireshark filters, scripting, web-security payloads, command injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Medium. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Strong. This covered XSS, SQL injection, mass assignment, SSRF, CSRF/SSRF, command injection, IDOR, and XXE questions.

Decision: Finalist

Reason:
Selected as a finalist because it had the best small-model overall score and stable trap performance.

---

## Qwen2.5-3B-Instruct

Status: Tested  
Size category: ≤7B  
Type: General-purpose instruct model  

Score summary:
- Normal score average: 3.96
- Trap score average: 4.22
- Overall average: 3.99
- Factual subset average: 4.14
- Practical subset average: 3.83
- Code-review trap average: 4.8
- Hallucination trap average: 3.5

Observations:
- Factual knowledge: Strong. This was judged from TCP, encryption, CVSS, IDS/IPS, TLS 1.3, threat terminology, and pentest methodology questions.
- Practical command quality: Medium to strong. This was judged from nmap, SUID search, Wireshark filters, scripting, web-security payloads, command injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Medium to strong. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Medium to strong. This covered XSS, SQL injection, mass assignment, SSRF, CSRF/SSRF, command injection, IDOR, and XXE questions.

Decision: Finalist

Reason:
Selected as a finalist because it was one of the strongest small models and had good trap performance.

---

## Qwen2.5-7B-Instruct

Status: Tested  
Size category: 7B–13B  
Type: General-purpose instruct model  

Score summary:
- Normal score average: 3.99
- Trap score average: 4.0
- Overall average: 3.99
- Factual subset average: 4.0
- Practical subset average: 3.79
- Code-review trap average: 5.0
- Hallucination trap average: 2.75

Observations:
- Factual knowledge: Strong. This was judged from TCP, encryption, CVSS, IDS/IPS, TLS 1.3, threat terminology, and pentest methodology questions.
- Practical command quality: Medium to strong. This was judged from nmap, SUID search, Wireshark filters, scripting, web-security payloads, command injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak to medium. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Medium to strong. This covered XSS, SQL injection, mass assignment, SSRF, CSRF/SSRF, command injection, IDOR, and XXE questions.

Decision: Comparison / not finalist

Reason:
Good model, but not selected because Qwen2.5-Coder provided stronger practical/code value.

---

## Qwen2.5-Coder-7B-Instruct

Status: Tested  
Size category: 7B–13B  
Type: Code-focused instruct model  

Score summary:
- Normal score average: 4.13
- Trap score average: 3.67
- Overall average: 4.08
- Factual subset average: 4.05
- Practical subset average: 4.54
- Code-review trap average: 5.0
- Hallucination trap average: 2.0

Observations:
- Factual knowledge: Strong. This was judged from TCP, encryption, CVSS, IDS/IPS, TLS 1.3, threat terminology, and pentest methodology questions.
- Practical command quality: Very strong. This was judged from nmap, SUID search, Wireshark filters, scripting, web-security payloads, command injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak to medium. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Medium to strong. This covered XSS, SQL injection, mass assignment, SSRF, CSRF/SSRF, command injection, IDOR, and XXE questions.

Decision: Finalist

Reason:
Selected as a finalist because it was one of the strongest models for code review and practical command tasks.

---

## SenecaLLM_x_Qwen2.5-7B-CyberSecurity

Status: Tested  
Size category: 7B–13B  
Type: Cybersecurity fine-tune  

Score summary:
- Normal score average: 4.04
- Trap score average: 3.67
- Overall average: 4.0
- Factual subset average: 4.0
- Practical subset average: 4.5
- Code-review trap average: 4.8
- Hallucination trap average: 2.25

Observations:
- Factual knowledge: Strong. This was judged from TCP, encryption, CVSS, IDS/IPS, TLS 1.3, threat terminology, and pentest methodology questions.
- Practical command quality: Very strong. This was judged from nmap, SUID search, Wireshark filters, scripting, web-security payloads, command injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak to medium. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Strong. This covered XSS, SQL injection, mass assignment, SSRF, CSRF/SSRF, command injection, IDOR, and XXE questions.

Decision: Comparison / not finalist

Reason:
Good cybersecurity-focused comparison, but not selected over Qwen2.5-Coder and Mistral-Nemo.

---

## TinyLlama-1.1B-Chat-v1.0

Status: Tested  
Size category: ≤7B  
Type: General-purpose chat baseline  

Score summary:
- Normal score average: 3.12
- Trap score average: 1.89
- Overall average: 2.97
- Factual subset average: 3.48
- Practical subset average: 2.5
- Code-review trap average: 2.6
- Hallucination trap average: 1.0

Observations:
- Factual knowledge: Medium. This was judged from TCP, encryption, CVSS, IDS/IPS, TLS 1.3, threat terminology, and pentest methodology questions.
- Practical command quality: Weak to medium. This was judged from nmap, SUID search, Wireshark filters, scripting, web-security payloads, command injection, and XXE tasks.
- Code review trap performance: Weak to medium. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Weak to medium. This covered XSS, SQL injection, mass assignment, SSRF, CSRF/SSRF, command injection, IDOR, and XXE questions.

Decision: Rejected baseline

Reason:
Useful as a weak baseline, but not reliable enough for professional cybersecurity work.

---

## WhiteRabbitNeo-2.5-Qwen-2.5-Coder-7B

Status: Tested  
Size category: 7B–13B  
Type: Coder / cybersecurity-oriented  

Score summary:
- Normal score average: 4.1
- Trap score average: 3.56
- Overall average: 4.04
- Factual subset average: 3.95
- Practical subset average: 4.17
- Code-review trap average: 4.8
- Hallucination trap average: 2.0

Observations:
- Factual knowledge: Medium to strong. This was judged from TCP, encryption, CVSS, IDS/IPS, TLS 1.3, threat terminology, and pentest methodology questions.
- Practical command quality: Strong. This was judged from nmap, SUID search, Wireshark filters, scripting, web-security payloads, command injection, and XXE tasks.
- Code review trap performance: Very strong. This measured whether the model found deeper issues rather than only obvious vulnerabilities.
- Hallucination trap performance: Weak to medium. This measured whether the model resisted fake CVEs and fictional attack names.
- Custom cybersecurity task performance: Medium to strong. This covered XSS, SQL injection, mass assignment, SSRF, CSRF/SSRF, command injection, IDOR, and XXE questions.

Decision: Comparison / not finalist

Reason:
Useful cybersecurity-oriented comparison, but not selected as a final model because it did not clearly outperform the strongest coder/general models.

---

## PHI-4-MINI-INSTRUCT

Status: Skipped  
Size category: ≤7B  
Type: General-purpose instruct model  

Observations:
- The model was downloaded, but it failed to load with the current `llama-cpp-python` CUDA backend.
- It was not evaluated, so no answer file or score table was produced.

Decision: Skipped

Reason:
The failure appears to be an inference-backend compatibility issue, not a model-quality result. The model was excluded from finalist selection.

---

## Screening Summary

The screening showed that model size alone did not determine quality. Some small models, especially Qwen2.5-3B and Phi-3.5-mini, performed competitively against larger models. TinyLlama was useful as a weak baseline but was rejected because it failed many practical and hallucination-trap questions.

The strongest overall baseline result came from Mistral-Nemo-Instruct-2407. Qwen2.5-Coder-7B-Instruct was the strongest practical/code-oriented finalist. Cybersecurity-focused models were useful for comparison, but they did not automatically outperform strong general-purpose or coder models. This supports the assignment warning that a cybersecurity label or willingness to answer is not enough; accuracy and hallucination resistance must be tested.
