# What Is Left To Finish

## Already completed

- Candidate models were tested.
- Baseline temperature `0` runs were completed.
- Finalists were selected.
- Temperature experiments at `0.5` and `1.0` were completed for the finalists.
- Raw answers are saved in `results/`.
- Automated evaluation output is saved in `report.md`.
- Summary tables were generated.

## Replace these files in the repository

Replace or add the following files from this package:

- `models_candidates.md`
- `screening_log.md`
- `final_report_baseline_analysis_draft.md`
- `temperature_experiments.md`
- `project_file_check.md`
- `data/model_score_summary_final.csv`
- `data/temperature_score_summary.csv`

## Check before final commit

1. `ask_llm.py` should have `TEMPERATURE = 0`.
2. Do not commit `*.gguf` model files.
3. Do not commit `venv/`.
4. Do not commit `.cache/`.
5. Keep `results/answers_*.json`.
6. Keep `report.md`.
7. Keep `data/temperature_score_summary.csv`.

## Optional cleanup

If `report.md` has duplicate or broken old sections, keep it as raw appendix and do not paste it into the final report. The final report should summarize it instead.

## Final Git commands

```powershell
git status
git add models_candidates.md screening_log.md final_report_baseline_analysis_draft.md temperature_experiments.md project_file_check.md data/model_score_summary_final.csv data/temperature_score_summary.csv
git status
git commit -m "Finalize LLM evaluation report and temperature analysis"
git push
```
