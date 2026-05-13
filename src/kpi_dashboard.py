import pandas as pd

DATA_PATH = "data/processed_device_financing_data.csv"

df = pd.read_csv(DATA_PATH)

total_customers = len(df)

total_loan_book = df["loan_amount_usd"].sum()

average_device_price = df["device_price_usd"].mean()

default_rate = (
    df["default_flag"].mean()
) * 100

high_risk_rate = (
    df["high_risk_flag"].mean()
) * 100

market_summary = (
    df.groupby("market")
    .agg({
        "loan_amount_usd": "sum",
        "customer_id": "count",
        "default_flag": "mean"
    })
    .rename(columns={
        "customer_id": "customer_count",
        "default_flag": "default_rate"
    })
)

market_summary["default_rate"] = (
    market_summary["default_rate"] * 100
).round(2)

print("\n========== EXECUTIVE KPI DASHBOARD ==========\n")

print(f"Total Customers: {total_customers}")

print(f"Total Loan Book (USD): ${total_loan_book:,.2f}")

print(f"Average Device Price (USD): ${average_device_price:.2f}")

print(f"Default Rate: {default_rate:.2f}%")

print(f"High Risk Rate: {high_risk_rate:.2f}%")

print("\n========== MARKET PERFORMANCE ==========\n")

print(market_summary.sort_values(
    by="loan_amount_usd",
    ascending=False
))