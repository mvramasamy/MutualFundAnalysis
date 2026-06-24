import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Check invalid NAV values
invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV records:", len(invalid_nav))

# Save cleaned file
df.to_csv("data/processed/cleaned_nav_history.csv", index=False)

print("NAV history cleaned successfully!")