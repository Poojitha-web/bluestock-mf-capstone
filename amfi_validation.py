import pandas as pd

# Load datasets
fund_master = pd.read_excel("Data/raw/01_fund_master.xlsx")
nav_history = pd.read_excel("Data/raw/02_nav_history.xlsx")

# Compare AMFI codes
master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("Total Fund Master Codes:", len(master_codes))
print("Total NAV History Codes:", len(nav_codes))
print("Missing Codes:", len(missing_codes))

if len(missing_codes) > 0:
    print("\nMissing AMFI Codes:")
    print(missing_codes)
else:
    print("\nAll AMFI codes are present in NAV history.")