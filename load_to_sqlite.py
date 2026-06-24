import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

pd.read_csv(
    "data/raw/01_fund_master.csv"
).to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/cleaned_nav_history.csv"
).to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/cleaned_investor_transactions.csv"
).to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully!")