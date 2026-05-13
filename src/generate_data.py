import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

markets = [
    "South Africa",
    "Tanzania",
    "Mozambique",
    "DRC",
    "Lesotho",
    "Kenya",
    "Ethiopia",
    "Egypt"
]

risk_segments = ["Low", "Medium", "High"]

data = []

for i in range(1000):
    device_price = random.randint(50, 1200)
    deposit_paid = random.randint(0, 300)

    loan_amount = device_price - deposit_paid

    days_past_due = max(0, int(np.random.normal(15, 20)))

    if days_past_due > 60:
        repayment_status = "Default"
        risk = "High"
    elif days_past_due > 30:
        repayment_status = "Late"
        risk = "Medium"
    else:
        repayment_status = "Current"
        risk = "Low"

    row = {
        "customer_id": fake.uuid4(),
        "market": random.choice(markets),
        "age": random.randint(18, 65),
        "tenure_months": random.randint(1, 120),
        "device_price_usd": device_price,
        "deposit_paid_usd": deposit_paid,
        "loan_amount_usd": loan_amount,
        "monthly_income_proxy": random.randint(100, 3000),
        "data_usage_gb": round(random.uniform(0.5, 50), 2),
        "mobile_money_txn_count": random.randint(0, 200),
        "days_past_due": days_past_due,
        "repayment_status": repayment_status,
        "risk_segment": risk
    }

    data.append(row)

df = pd.DataFrame(data)

df.to_csv("data/device_financing_data.csv", index=False)

print("Synthetic dataset generated successfully.")
print(df.head())