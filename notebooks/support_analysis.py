# Support Operations Analysis
# This script analyses support ticket data to identify operational bottlenecks,
# including average resolution times and SLA breaches.

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def main() -> None:
    # Resolve paths relative to this file (works from any working directory)
    base_dir = Path(__file__).resolve().parent.parent  # repo root
    data_path = base_dir / "data" / "support_tickets_large.csv"

    output_dir = base_dir / "outputs"
    output_dir.mkdir(exist_ok=True)

    print("Loading dataset from:", data_path)
    df = pd.read_csv(data_path)

    print("Rows:", len(df))
    print(df.head())

    # Average resolution time by issue type
    avg_resolution = (
        df.groupby("issue_type")["resolution_time_hours"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\nAverage resolution time (hours) by issue type:")
    print(avg_resolution)

    # Plot: average resolution time
    plt.figure()
    avg_resolution.plot(kind="bar")
    plt.title("Average Resolution Time by Issue Type")
    plt.ylabel("Hours")
    plt.xlabel("Issue Type")
    plt.tight_layout()
    plt.savefig(output_dir / "avg_resolution_time_by_issue.png")
    plt.close()

    # SLA breach rate (>4 hours)
    df["sla_breach"] = df["resolution_time_hours"] > 4
    sla_by_issue = (
        df.groupby("issue_type")["sla_breach"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\nSLA breach rate by issue type:")
    print(sla_by_issue)

    # Plot: SLA breach rate
    plt.figure()
    sla_by_issue.plot(kind="bar")
    plt.title("SLA Breach Rate (>4 hours) by Issue Type")
    plt.ylabel("Breach Rate")
    plt.xlabel("Issue Type")
    plt.tight_layout()
    plt.savefig(output_dir / "sla_breach_rate_by_issue.png")
    plt.close()

    print("\nSaved charts to:", output_dir)


if __name__ == "__main__":
    main()
