# LLM Cybersecurity Evaluation

This repository contains our local LLM evaluation for cybersecurity tasks.

We compared general-purpose, coder, and cybersecurity-oriented models using the same local evaluation pipeline.

Included materials:

- candidate model reconnaissance
- screening results
- full evaluation results
- temperature experiments
- custom cybersecurity criteria
- raw model outputs
- score summaries
- final report in Markdown format

## Actual Test Environment

We ran the evaluation locally on a Windows laptop using `llama-cpp-python` with CUDA support.

Models were downloaded from Hugging Face in GGUF format, mostly with Q4_K_M quantization. We used this format because it was realistic for our hardware and still gave usable answer quality.

Local setup:

- Windows
- Python virtual environment
- `llama-cpp-python`
- CUDA-enabled `llama-cpp-python`
- NVIDIA RTX laptop GPU
- Hugging Face GGUF models
- Q4_K_M quantization where available

We did not use commercial APIs to generate model answers. All tested outputs were generated locally.

## Main Files

| File / Folder | Purpose |
|---|---|
| `ask_llm.py` | Loads a local GGUF model, asks all questions, saves responses |
| `evaluate_llm.py` | Evaluates model answers against reference answers |
| `summarize_scores.py` | Produces score summaries |
| `questions.json` | Full evaluation question set |
| `answers.json` | Reference answers |
| `custom_questions_report.md` | Explanation of custom questions |
| `models_candidates.md` | Candidate model list and reconnaissance notes |
| `screening_log.md` | Screening decisions and reasoning |
| `temperature_experiments.md` | Temperature experiment summary |
| `report.md` | Final Markdown report |
| `data/` | Score summary CSV files |
| `results/` | Raw model outputs in JSON |
| `reports/` | Intermediate report backups |

## Pipeline

### 1. Generate model answers

Run:

    python ask_llm.py

The script asks for a Hugging Face GGUF model URL, downloads or locates the model, runs all questions, and saves responses to:

    answers_llm.json

### 2. Evaluate answers

Run:

    python evaluate_llm.py

The evaluator reads:

    answers_llm.json

and appends results to:

    report.md

### 3. Summarize scores

Run:

    python summarize_scores.py

Score summaries are saved in:

    data/

## Evaluation Settings

| Parameter | Value |
|---|---|
| Max tokens | 1024 |
| Context window | 4096 |
| Baseline temperature | 0 |
| Temperature experiments | 0, 0.5, 1.0 |
| Evaluator temperature | 0.1 |
| Quantization | mostly GGUF Q4_K_M |

## Submission Files

The main submission report is:

    final_report.md

The detailed automated evaluation output is:

    automated_evaluation_report.md

Supporting evidence is stored in:

    models_candidates.md
    screening_log.md
    temperature_experiments.md
    data/
    results/
    reports/

## Notes

Large model files are not included in the repository.

The repository should not contain:

- `venv/`
- `.gguf` files
- Hugging Face cache
- CUDA installer files
- temporary backup folders