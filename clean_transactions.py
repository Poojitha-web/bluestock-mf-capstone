import pandas as pd

df = pd.read_excel(
    "Data/raw/08_investor_transactions.xlsx"
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Fix date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Amount validation
df = df[df["amount_inr"] > 0]

# KYC validation
valid_kyc = ["Verified", "Pending"]

invalid_kyc = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print("Invalid KYC:", len(invalid_kyc))

df.to_csv(
    "Data/processed/08_transactions_clean.csv",
    index=False
)

print("Transactions cleaned")