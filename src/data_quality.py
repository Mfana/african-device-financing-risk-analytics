import pandas as pd

DATA_PATH = "data/device_financing_data.csv"

VALID_MARKETS = {
    "South Africa",
    "Tanzania",
    "Mozambique",
    "DRC",
    "Lesotho",
    "Kenya",
    "Ethiopia",
    "Egypt"
}

VALID_REPAYMENT_STATUS = {"Current", "Late", "Default"}
VALID_RISK_SEGMENTS = {"Low", "Medium", "High"}


def run_data_quality_checks():
    df = pd.read_csv(DATA_PATH)

    checks = {
        "dataset_not_empty": len(df) > 0,
        "customer_id_not_null": df["customer_id"].notnull().all(),
        "customer_id_unique": df["customer_id"].is_unique,
        "valid_markets": df["market"].isin(VALID_MARKETS).all(),
        "age_reasonable": df["age"].between(18, 65).all(),
        "device_price_positive": (df["device_price_usd"] > 0).all(),
        "deposit_paid_non_negative": (df["deposit_paid_usd"] >= 0).all(),
        "loan_amount_non_negative": (df["loan_amount_usd"] >= 0).all(),
        "loan_amount_matches_price_minus_deposit": (
            df["loan_amount_usd"] == df["device_price_usd"] - df["deposit_paid_usd"]
        ).all(),
        "days_past_due_non_negative": (df["days_past_due"] >= 0).all(),
        "valid_repayment_status": df["repayment_status"].isin(VALID_REPAYMENT_STATUS).all(),
        "valid_risk_segments": df["risk_segment"].isin(VALID_RISK_SEGMENTS).all(),
    }

    failed_checks = [check for check, passed in checks.items() if not passed]

    if failed_checks:
        print("Data quality checks failed:")
        for check in failed_checks:
            print(f"- {check}")
        raise ValueError("Data quality validation failed.")

    print("All data quality checks passed successfully.")


if __name__ == "__main__":
    run_data_quality_checks()