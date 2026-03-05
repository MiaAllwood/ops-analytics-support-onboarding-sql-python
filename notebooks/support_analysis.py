# Support Operations Analysis
# This script analyses support ticket data to identify operational bottlenecks,
# including average resolution times and SLA breaches.

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (relative path from /notebooks folder)
df = pd.read_csv("../data/support_tickets.csv")

# Basic checks
print("Rows:", len(df))
print(df.head())

# Average resolution time by issue type
avg_resolution = df.groupby("issue_type")["resolution_time_hours"].mean().sort_values(ascending=False)
print("\nAverage resolution time (hours) by issue type:")
print(avg_resolution)

# Plot average resolution time
avg_resolution.plot(kind="bar")
plt.title("Average Resolution Time by Issue Type")
plt.ylabel("Hours")
plt.xlabel("Issue Type")
plt.tight_layout()
plt.show()

# SLA breach rate (4 hour SLA)
df["sla_breach"] = df["resolution_time_hours"] > 4
sla_rate = df["sla_breach"].mean()

print(f"\nSLA breach rate (>4 hours): {sla_rate:.0%}")

# SLA breach rate by issue type
sla_by_issue = df.groupby("issue_type")["sla_breach"].mean().sort_values(ascending=False)
print("\nSLA breach rate by issue type:")
print(sla_by_issue)

# Plot SLA breach rate by issue type
sla_by_issue.plot(kind="bar")
plt.title("SLA Breach Rate (>4 hours) by Issue Type")
plt.ylabel("Breach Rate")
plt.xlabel("Issue Type")
plt.tight_layout()
plt.show()
