# Project File Check

## Required Deliverables

### 1. Main Report

Main report file:

- `report.md`

The report covers:

- goal of the study
- models overview
- experimental setup
- prompt set
- evaluation criteria
- quantitative results
- qualitative results
- temperature experiments
- comparison by category
- impact of model size
- limitations
- conclusion
- discussion

### 2. Python Code

The main pipeline files are:

- `ask_llm.py`
- `evaluate_llm.py`
- `summarize_scores.py`

These files provide the evaluation workflow:

1. load a local GGUF model
2. ask all questions
3. save model responses
4. evaluate responses against reference answers
5. summarize scores

### 3. Raw Data

Raw model outputs are stored in:

- `results/answers_*.json`

Score summaries are stored in:

- `data/model_score_summary.csv`
- `data/model_score_summary_extended.csv`
- `data/model_score_summary_final.csv`
- `data/temperature_score_summary.csv`

### 4. Supporting Files

Supporting project files:

- `questions.json`
- `answers.json`
- `custom_questions_report.md`
- `models_candidates.md`
- `screening_log.md`
- `temperature_experiments.md`
- `requirements.txt`
- `README.md`

## Repository Cleanliness Check

The repository should NOT include:

- `venv/`
- `.cache/`
- `__pycache__/`
- `.gguf` model files
- Hugging Face cache
- CUDA installer files
- temporary backup folders
- temporary unfinished `answers_llm.json`

## Final Check Commands

Before submission, run:

```powershell
git status
```

Check that no large model files are included:

```powershell
Get-ChildItem -Recurse -Include *.gguf | Select-Object FullName
```

Check that no virtual environment is included:

```powershell
Test-Path venv
```

Expected result:

```text
No .gguf files listed
Test-Path venv = False
```

## Submission Package

Recommended submission:

- `report.md`
- GitHub repository link
- presentation file if required separately