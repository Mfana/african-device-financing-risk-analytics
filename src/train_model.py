import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

DATA_PATH = "data/processed_device_financing_data.csv"

df = pd.read_csv(DATA_PATH)

features = [
    "tenure_months",
    "device_price_usd",
    "deposit_paid_usd",
    "loan_amount_usd",
    "monthly_income_proxy",
    "data_usage_gb",
    "mobile_money_txn_count",
    "days_past_due",
    "deposit_ratio",
    "loan_to_income_ratio"
]

target = "default_flag"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\n========== MODEL PERFORMANCE ==========\n")

print(f"Accuracy: {accuracy:.2f}")

print("\nClassification Report:\n")

print(classification_report(y_test, predictions))