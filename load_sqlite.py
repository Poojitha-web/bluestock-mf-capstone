import pandas as pd
from sqlalchemy import create_engine

# Create database connection
engine = create_engine("sqlite:///db/bluestock_mf.db")

# Load datasets
fund_master = pd.read_excel("Data/raw/01_fund_master.xlsx")
nav_history = pd.read_csv("Data/processed/02_nav_history_clean.csv")
aum = pd.read_excel("Data/raw/03_aum_by_fund_house.xlsx")
performance = pd.read_csv("Data/processed/07_scheme_performance_clean.csv")
transactions = pd.read_csv("Data/processed/08_transactions_clean.csv")

# Load into SQLite
fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("All datasets loaded successfully!")