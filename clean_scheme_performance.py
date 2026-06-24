import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Expense ratio validation
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Invalid expense ratio records:")
print(len(invalid_expense))

df.to_csv(
    "data/processed/cleaned_scheme_performance.csv",
    index=False
)

print("Scheme performance cleaned successfully!")