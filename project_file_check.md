# Project File Check

## Summary

This check was made from the uploaded final review archive.

## Required project files

| File / Folder | Status | Notes |
|---|---|---|
| `report.md` | Present | Contains baseline evaluations and temperature experiment evaluations. |
| `questions.json` | Present | Contains 32 evaluation questions. |
| `answers.json` | Present | Contains 22 reference answers for the core question set. |
| `ask_llm.py` | Present | Uses a shared `TEMPERATURE` variable and CUDA offloading through `n_gpu_layers=-1`. |
| `evaluate_llm.py` | Present | Uses the same evaluator settings for all runs. |
| `results/answers_*.json` | Present | 20 answer files found. All contain 32 answers. |
| `data/model_score_summary.csv` | Present | Baseline score summary. |
| `data/model_score_summary_extended.csv` | Present | Extended baseline category summary. |
| `models_candidates.md` | Replaced by new version | Uploaded version had only three model rows. Replacement file contains the full candidate table. |
| `screening_log.md` | Replaced by new version | Replacement file contains complete screening decisions. |
| `final_report_baseline_analysis_draft.md` | Replaced by new version | Replacement file contains the final report text with temperature experiments. |
| `temperature_experiments.md` | New file | Added summary and interpretation of temperature experiments. |

## Raw answer file validation

| File | Answers | Status |
|---|---:|---|
| `answers_gemma_2_9b_it_temp0.json` | 32 | OK |
| `answers_lily_cybersecurity_7b_temp0.json` | 32 | OK |
| `answers_llama_3_2_3b_temp0.json` | 32 | OK |
| `answers_mistral_7b_temp0.json` | 32 | OK |
| `answers_mistral_nemo_12b_temp0.json` | 32 | OK |
| `answers_mistral_nemo_12b_temp05.json` | 32 | OK |
| `answers_mistral_nemo_12b_temp10.json` | 32 | OK |
| `answers_phi_3_5_mini_temp0.json` | 32 | OK |
| `answers_phi_3_5_mini_temp05.json` | 32 | OK |
| `answers_phi_3_5_mini_temp10.json` | 32 | OK |
| `answers_qwen_2_5_3b_temp0.json` | 32 | OK |
| `answers_qwen_2_5_3b_temp05.json` | 32 | OK |
| `answers_qwen_2_5_3b_temp10.json` | 32 | OK |
| `answers_qwen_2_5_7b_temp0.json` | 32 | OK |
| `answers_qwen_2_5_coder_7b_temp0.json` | 32 | OK |
| `answers_qwen_2_5_coder_7b_temp05.json` | 32 | OK |
| `answers_qwen_2_5_coder_7b_temp10.json` | 32 | OK |
| `answers_seneca_qwen_2_5_7b_cybersecurity_temp0.json` | 32 | OK |
| `answers_tinyllama_temp0.json` | 32 | OK |
| `answers_whiterabbitneo_2_5_qwen_coder_7b_temp0.json` | 32 | OK |

## Notes

- `Phi-4-mini-instruct` was attempted but not included as an evaluated model because it failed to load with the current CUDA backend.
- `report.md` is large and can be kept as the automated scoring appendix.
- The final report should not paste the full `report.md`; it should summarize the results and refer to raw files and `report.md`.
- Before final commit, keep `ask_llm.py` at `TEMPERATURE = 0` so the project defaults back to the baseline setting.
