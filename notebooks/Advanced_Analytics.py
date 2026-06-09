import pandas as pd
import numpy as np

nav = pd.read_excel("../Data/raw/02_nav_history.xlsx")

nav['date'] = pd.to_datetime(nav['date'])
nav = nav.sort_values(['amfi_code','date'])

nav['daily_return'] = nav.groupby('amfi_code')['nav'].pct_change()

var95 = nav.groupby('amfi_code')['daily_return'].quantile(0.05)

print("95% Value at Risk")
print(var95.head())

var95.to_csv("../reports/var95.csv")

transactions = pd.read_excel("../Data/raw/08_investor_transactions.xlsx")

cohort = transactions.groupby(
    ['age_group','city_tier']
)['amount_inr'].sum().reset_index()

print(cohort.head())

performance = pd.read_excel("../Data/raw/07_scheme_performance.xlsx")

recommended = performance.sort_values(
    'return_3yr_pct',
    ascending=False
).head(10)

print(recommended[['scheme_name','return_3yr_pct']])

recommended.to_csv("../reports/recommended_funds.csv", index=False)