import pandas as pd

df = pd.read_excel(
    "Data/raw/07_scheme_performance.xlsx"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Expense ratio validation
anomalies = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

print("Expense Ratio Anomalies")
print(len(anomalies))

df.to_csv(
    "Data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned")