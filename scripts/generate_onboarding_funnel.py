import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

countries = ["UK", "Germany", "France", "Spain", "Italy"]
channels = ["organic", "paid_search", "paid_social", "referral", "partnership"]
devices = ["iOS", "Android", "Web"]

rows = []
start_date = datetime(2024, 1, 1)

# Generate 2000 synthetic user journeys
for user_id in range(20001, 22001):
    signup = start_date + timedelta(minutes=random.randint(0, 800000))
    country = random.choice(countries)
    channel = random.choice(channels)
    device = random.choice(devices)

    # probabilities (make it realistic-ish)
    p_kyc_start = 0.88
    p_kyc_complete_given_start = 0.82
    p_first_txn_given_kyc_complete = 0.70

    # Slightly lower conversion on Web and for paid channels (synthetic realism)
    if device == "Web":
        p_kyc_complete_given_start -= 0.07
        p_first_txn_given_kyc_complete -= 0.05
    if channel in ["paid_social", "paid_search"]:
        p_first_txn_given_kyc_complete -= 0.04

    kyc_started = random.random() < p_kyc_start
    kyc_completed = False
    first_transaction = False

    kyc_started_at = None
    kyc_completed_at = None
    first_transaction_at = None

    if kyc_started:
        kyc_started_at = signup + timedelta(minutes=random.randint(1, 240))  # within 4 hours
        kyc_completed = random.random() < p_kyc_complete_given_start

        if kyc_completed:
            # KYC completion time varies by country a bit
            base_minutes = random.randint(10, 600)  # 10 min to 10 hours
            if country in ["France", "Italy"]:
                base_minutes += random.randint(20, 180)
            kyc_completed_at = kyc_started_at + timedelta(minutes=base_minutes)

            first_transaction = random.random() < p_first_txn_given_kyc_complete
            if first_transaction:
                first_transaction_at = kyc_completed_at + timedelta(minutes=random.randint(30, 10080))  # up to 7 days

    rows.append({
        "user_id": user_id,
        "country": country,
        "acquisition_channel": channel,
        "device": device,
        "signup_at": signup,
        "kyc_started_at": kyc_started_at,
        "kyc_completed_at": kyc_completed_at,
        "first_transaction_at": first_transaction_at
    })

df = pd.DataFrame(rows)
df.to_csv("data/onboarding_funnel_large.csv", index=False)

print("Dataset created: data/onboarding_funnel_large.csv")
