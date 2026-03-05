# Support Operations Analysis
# This script analyses support ticket data to identify operational bottlenecks

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
df = pd.read_csv(BASE_DIR / "data" / "support_tickets_large.csv")

df = pd.read_csv("../data/support_tickets_large.csv")

print("Rows:", len(df))
print(df.head())

# Average resolution time by issue type
avg_resolution = df.groupby("issue_type")["resolution_time_hours"].mean().sort_values(ascending=False)

print("\nAverage resolution time (hours) by issue type:")
print(avg_resolution)

# Plot average resolution time
plt.figure()
avg_resolution.plot(kind="bar")
plt.title("Average Resolution Time by Issue Type")
plt.ylabel("Hours")
plt.xlabel("Issue Type")
plt.tight_layout()

plt.savefig("../outputs/avg_resolution_time_by_issue.png")

plt.close()

# SLA breach rate
df["sla_breach"] = df["resolution_time_hours"] > 4
sla_by_issue = df.groupby("issue_type")["sla_breach"].mean().sort_values(ascending=False)

print("\nSLA breach rate by issue type:")
print(sla_by_issue)

plt.figure()
sla_by_issue.plot(kind="bar")
plt.title("SLA Breach Rate (>4 hours) by Issue Type")
plt.ylabel("Breach Rate")
plt.xlabel("Issue Type")
plt.tight_layout()

plt.savefig("../outputs/sla_breach_rate_by_issue.png")

plt.close()
