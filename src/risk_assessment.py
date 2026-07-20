"""
IT Risk Assessment Lab
-----------------------
Reads an asset/threat/vulnerability register, calculates a risk score for
each entry using a standard Likelihood x Impact model, assigns a risk
rating, and produces a prioritized risk register plus a summary chart.

Risk scoring model:
    Risk Score = Likelihood (1-5) x Impact (1-5)
    1-6   -> Low
    7-14  -> Medium
    15-25 -> High

This mirrors the approach used in common frameworks such as NIST SP 800-30
(qualitative likelihood/impact risk analysis) and is a standard method used
in IT audit and GRC risk assessments.

Run from the repository root:
    python src/risk_assessment.py
"""

import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE = os.path.join(BASE_DIR, "data", "assets_risks.csv")
OUTPUT_CSV = os.path.join(BASE_DIR, "output", "risk_register_prioritized.csv")
OUTPUT_CHART = os.path.join(BASE_DIR, "output", "risk_summary_chart.png")


def risk_rating(score):
    if score >= 15:
        return "High"
    elif score >= 7:
        return "Medium"
    else:
        return "Low"


def load_risks(path):
    risks = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            likelihood = int(row["likelihood"])
            impact = int(row["impact"])
            score = likelihood * impact
            row["risk_score"] = score
            row["risk_rating"] = risk_rating(score)
            risks.append(row)
    return risks


def write_prioritized_register(risks, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fieldnames = [
        "asset_id", "asset_name", "category", "threat", "vulnerability",
        "likelihood", "impact", "risk_score", "risk_rating", "existing_control",
    ]
    ranked = sorted(risks, key=lambda r: r["risk_score"], reverse=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in ranked:
            writer.writerow({k: row[k] for k in fieldnames})
    return ranked


def print_summary(ranked):
    counts = {"High": 0, "Medium": 0, "Low": 0}
    for r in ranked:
        counts[r["risk_rating"]] += 1

    print("=" * 70)
    print("IT RISK ASSESSMENT - PRIORITIZED RISK REGISTER")
    print("=" * 70)
    print(f"{'Asset':<28}{'Threat':<24}{'Score':<8}{'Rating'}")
    print("-" * 70)
    for r in ranked:
        print(f"{r['asset_name']:<28}{r['threat']:<24}{r['risk_score']:<8}{r['risk_rating']}")
    print("-" * 70)
    print(f"Total risks: {len(ranked)}  |  High: {counts['High']}  "
          f"Medium: {counts['Medium']}  Low: {counts['Low']}")
    print("=" * 70)


def make_chart(ranked):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed, skipping chart generation.")
        return

    colors = {"High": "#c0392b", "Medium": "#e67e22", "Low": "#27ae60"}
    names = [r["asset_name"] for r in ranked]
    scores = [r["risk_score"] for r in ranked]
    bar_colors = [colors[r["risk_rating"]] for r in ranked]

    plt.figure(figsize=(9, 6))
    plt.barh(names, scores, color=bar_colors)
    plt.xlabel("Risk Score (Likelihood x Impact)")
    plt.title("IT Risk Assessment - Risk Score by Asset")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    os.makedirs(os.path.dirname(OUTPUT_CHART), exist_ok=True)
    plt.savefig(OUTPUT_CHART, dpi=150)
    print(f"Chart saved to {OUTPUT_CHART}")


if __name__ == "__main__":
    risks = load_risks(INPUT_FILE)
    ranked = write_prioritized_register(risks, OUTPUT_CSV)
    print_summary(ranked)
    make_chart(ranked)
    print(f"\nPrioritized risk register written to {OUTPUT_CSV}")
