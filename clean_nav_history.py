import pandas as pd

df = pd.read_excel("Data/raw/02_nav_history.xlsx")

# Date conversion
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Validate NAV
invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV Rows:", len(invalid_nav))

# Save
df.to_csv(
    "Data/processed/02_nav_history_clean.csv",
    index=False
)

print("NAV history cleaned successfully")