import pandas as pd

files = [
    "01_fund_master.xlsx",
    "02_nav_history.xlsx",
    "03_aum_by_fund_house.xlsx",
    "07_scheme_performance.xlsx",
    "08_investor_transactions.xlsx"
]

for file in files:
    print("\n", file)
    df = pd.read_excel(f"Data/raw/{file}")
    print(df.columns.tolist())