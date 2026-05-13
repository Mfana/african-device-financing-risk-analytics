import pandas as pd

RAW_DATA_PATH = "data/device_financing_data.csv"
PROCESSED_DATA_PATH = "data/processed_device_financing_data.csv"


def run_etl_pipeline():
    df = pd.read_csv(RAW_DATA_PATH)

    df["deposit_ratio"] = df["deposit_paid_usd"] / df["device_price_usd"]
    df["loan_to_income_ratio"] = df["loan_amount_usd"] / df["monthly_income_proxy"]

    df["high_risk_flag"] = df["risk_segment"].apply(
        lambda x: 1 if x == "High" else 0
    )

    df["default_flag"] = df["repayment_status"].apply(
        lambda x: 1 if x == "Default" else 0
    )

    df["market"] = df["market"].str.strip()

    df.to_csv(PROCESSED_DATA_PATH, index=False)

    print("ETL pipeline completed successfully.")
    print(df.head())


if __name__ == "__main__":
    run_etl_pipeline()