from pathlib import Path
import re
import csv

report_path = Path("report.md")
out_path = Path("data/model_score_summary.csv")

out_path.parent.mkdir(exist_ok=True)

text = report_path.read_text(encoding="utf-8")

sections = re.split(r"\n## Model Evaluation:\s*", text)
rows = []

for section in sections[1:]:
    lines = section.splitlines()
    if not lines:
        continue

    model_name = lines[0].strip()

    normal_scores = []
    trap_scores = []

    for line in lines:
        if not line.startswith("| Q"):
            continue

        parts = [p.strip() for p in line.strip().split("|")]
        if len(parts) < 7:
            continue

        qid = parts[1]
        accuracy = parts[2]
        completeness = parts[3]
        practicality = parts[4]
        trap = parts[5]

        if trap != "-" and trap.isdigit():
            trap_scores.append(int(trap))
        else:
            nums = []
            for value in [accuracy, completeness, practicality]:
                if value.isdigit():
                    nums.append(int(value))
            if nums:
                normal_scores.extend(nums)

    avg_normal = round(sum(normal_scores) / len(normal_scores), 2) if normal_scores else ""
    avg_trap = round(sum(trap_scores) / len(trap_scores), 2) if trap_scores else ""
    avg_total_values = normal_scores + trap_scores
    avg_total = round(sum(avg_total_values) / len(avg_total_values), 2) if avg_total_values else ""

    rows.append({
        "Model": model_name,
        "Normal Score Average": avg_normal,
        "Trap Score Average": avg_trap,
        "Overall Average": avg_total,
        "Normal Score Count": len(normal_scores),
        "Trap Question Count": len(trap_scores),
    })

with out_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "Model",
        "Normal Score Average",
        "Trap Score Average",
        "Overall Average",
        "Normal Score Count",
        "Trap Question Count",
    ])
    writer.writeheader()
    writer.writerows(rows)

print(f"Saved summary to {out_path}")
for row in rows:
    print(row)