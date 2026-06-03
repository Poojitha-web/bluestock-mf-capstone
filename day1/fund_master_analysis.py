import pandas as pd
from pathlib import Path

# Fund master file path
file_path = Path("Data/raw/01_fund_master.xlsx")

# Read Excel file
fund_master = pd.read_excel(file_path)

print("=" * 50)
print("Fund Master Dataset Loaded Successfully")
print("=" * 50)

print("\nColumns:")
print(fund_master.columns.tolist())

print("\nShape:")
print(fund_master.shape)

# Check if expected columns exist before printing
if "fund_house" in fund_master.columns:
    print("\nFund Houses:")
    print(fund_master["fund_house"].unique())

if "category" in fund_master.columns:
    print("\nCategories:")
    print(fund_master["category"].unique())

if "sub_category" in fund_master.columns:
    print("\nSub Categories:")
    print(fund_master["sub_category"].unique())

if "risk_category" in fund_master.columns:
    print("\nRisk Categories:")
    print(fund_master["risk_category"].unique())