import pandas as pd
import random
from datetime import datetime, timedelta

countries = ["UK", "Germany", "France", "Spain", "Italy"]
issue_types = ["card_declined", "kyc_verification", "login_issue", "payment_failed"]
channels = ["chat", "email", "phone"]
priorities = ["low", "medium", "high", "critical"]

rows = []

start_date = datetime(2024, 1, 1)

for i in range(1, 1001):

    created = start_date + timedelta(minutes=random.randint(0, 500000))
    resolution_hours = round(random.uniform(0.3, 12), 2)
    resolved = created + timedelta(hours=resolution_hours)

    rows.append({
        "ticket_id": i,
        "user_id": random.randint(1000, 5000),
        "country": random.choice(countries),
        "issue_type": random.choice(issue_types),
        "channel": random.choice(channels),
        "priority": random.choice(priorities),
        "created_at": created,
        "resolved_at": resolved,
        "resolution_time_hours": resolution_hours,
        "status": "resolved"
    })

df = pd.DataFrame(rows)

df.to_csv("data/support_tickets_large.csv", index=False)

print("Dataset created: data/support_tickets_large.csv")
