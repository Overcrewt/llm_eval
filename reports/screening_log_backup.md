# Screening Log

The screening phase was used to quickly test candidate models before selecting finalists for full evaluation.

Each model was checked on a smaller set of questions from different categories:

- Q1 — factual / TCP handshake
- Q4 — practical / nmap command
- Q8 — conceptual / IDS vs IPS
- Q11 — sensitive / SQL injection
- Q13 — sensitive / reverse shell
- Q16 — code review trap
- Q20 — hallucination trap
- Q23 — custom sensitive / XSS payload

## TinyLlama-1.1B-Chat-v1.0

Status: Tested

Decision: Pending

Notes:
- Basic factual answers:
- Practical command quality:
- Sensitive question behavior:
- Trap question behavior:
- Final decision:

Phi-4-mini-instruct was downloaded successfully, but failed to load with the current llama-cpp-python CUDA build. The model was skipped because the issue appears to be compatibility with the local inference backend rather than model output quality.