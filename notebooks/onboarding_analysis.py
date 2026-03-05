import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/onboarding_funnel_large.csv")

# Convert timestamps
for col in ["signup_at", "kyc_started_at", "kyc_completed_at", "first_transaction_at"]:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Funnel counts
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

# Plot funnel
plt.figure()
funnel.plot(kind="bar")
plt.title("Onboarding Funnel (Counts)")
plt.ylabel("Users")
plt.tight_layout()
plt.savefig("../outputs/onboarding_funnel_counts.png")
plt.close()
print("Saved: ../outputs/onboarding_funnel_counts.png")

# Time to complete KYC (minutes)
kyc = df[df["kyc_started_at"].notna() & df["kyc_completed_at"].notna()].copy()
kyc["kyc_minutes"] = (kyc["kyc_completed_at"] - kyc["kyc_started_at"]).dt.total_seconds() / 60

by_country = kyc.groupby("country")["kyc_minutes"].mean().sort_values(ascending=False)
print("\nAverage KYC time (minutes) by country:")
print(by_country.round(2))

plt.figure()
by_country.plot(kind="bar")
plt.title("Average KYC Completion Time by Country")
plt.ylabel("Minutes")
plt.tight_layout()
plt.savefig("../outputs/avg_kyc_time_by_country.png")
plt.close()
print("Saved: ../outputs/avg_kyc_time_by_country.png")

# Signup -> First transaction rate by channel
df["has_first_txn"] = df["first_transaction_at"].notna()
by_channel = df.groupby("acquisition_channel")["has_first_txn"].mean().sort_values(ascending=False)

print("\nSignup -> First transaction rate by channel:")
print(by_channel.round(4))

plt.figure()
by_channel.plot(kind="bar")
plt.title("Signup → First Transaction Rate by Acquisition Channel")
plt.ylabel("Conversion Rate")
plt.tight_layout()
plt.savefig("../outputs/first_txn_rate_by_channel.png")
plt.close()
print("Saved: ../outputs/first_txn_rate_by_channel.png")
