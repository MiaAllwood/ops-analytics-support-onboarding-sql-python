import os
import pandas as pd
import matplotlib.pyplot as plt

# Always create outputs folder (relative to repo root when running the script)
os.makedirs("../outputs", exist_ok=True)

df = pd.read_csv("data/onboarding_funnel_large.csv")

for col in ["signup_at", "kyc_started_at", "kyc_completed_at", "first_transaction_at"]:
    df[col] = pd.to_datetime(df[col], errors="coerce")

signups = len(df)
kyc_started = df["kyc_started_at"].notna().sum()
kyc_completed = df["kyc_completed_at"].notna().sum()
first_txn = df["first_transaction_at"].notna().sum()

funnel = pd.Series(
    [signups, kyc_started, kyc_completed, first_txn],
    index=["Signups", "KYC Started", "KYC Completed", "First Transaction"]
)

print("\nFunnel counts:")
print(funnel)

plt.figure()
funnel.plot(kind="bar")
plt.title("Onboarding Funnel (Counts)")
plt.ylabel("Users")
plt.tight_layout()

plt.savefig("../outputs/onboarding_funnel_counts.png")
plt.close()

print("\nSaved: ../outputs/onboarding_funnel_counts.png")
