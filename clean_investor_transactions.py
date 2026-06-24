import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Remove invalid amounts
df = df[df["amount_inr"] > 0]

print("Transaction Types:")
print(df["transaction_type"].unique())

print("\nKYC Status:")
print(df["kyc_status"].unique())

df.to_csv(
    "data/processed/cleaned_investor_transactions.csv",
    index=False
)

print("Investor transactions cleaned successfully!")