import matplotlib
matplotlib.use("Agg")
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go
import os

print("Current Working Directory:", os.getcwd())

os.makedirs("../reports/charts", exist_ok=True)

print("Charts folder created/exists")
sns.set_style("whitegrid")
fund_master = pd.read_excel("../Data/raw/01_fund_master.xlsx")

nav = pd.read_csv("../Data/processed/02_nav_history_clean.csv")

aum = pd.read_excel("../Data/raw/03_aum_by_fund_house.xlsx")

sip = pd.read_excel("../Data/raw/04_monthly_sip_inflows.xlsx")

category = pd.read_excel("../Data/raw/05_category_inflows.xlsx")

folio = pd.read_excel("../Data/raw/06_industry_folio_count.xlsx")

performance = pd.read_csv("../Data/processed/07_scheme_performance_clean.csv")

transactions = pd.read_csv("../Data/processed/08_transactions_clean.csv")

portfolio = pd.read_excel("../Data/raw/09_portfolio_holdings.xlsx")

benchmark = pd.read_excel("../Data/raw/10_benchmark_indices.xlsx")
print("All datasets loaded successfully!")
print("Fund Master:", fund_master.shape)
print("NAV:", nav.shape)
print("AUM:", aum.shape)
print("SIP:", sip.shape)
print("Transactions:", transactions.shape)
# Chart 1: NAV Trend Analysis

nav["date"] = pd.to_datetime(nav["date"])

fig = px.line(
    nav,
    x="date",
    y="nav",
    color="amfi_code",
    title="Daily NAV Trend for 40 Mutual Fund Schemes (2022-2026)"
)
fig.write_image("../reports/charts/nav_trend.png")
fig.show()
# Insight 1:
# Most mutual fund schemes exhibited a long-term upward NAV trend
# from 2022 to 2026, indicating consistent wealth creation despite
# short-term market fluctuations.

# Chart 2: AUM Growth by Fund House

# Convert date column
aum["date"] = pd.to_datetime(aum["date"])

# Extract year
aum["year"] = aum["date"].dt.year

plt.figure(figsize=(14,6))

sns.barplot(
    data=aum,
    x="year",
    y="aum_lakh_crore",
    hue="fund_house"
)

plt.title("AUM Growth by Fund House (2022–2025)")
plt.xlabel("Year")
plt.ylabel("AUM (Lakh Crore)")
plt.xticks(rotation=45)

plt.tight_layout()

# Save chart
plt.savefig("../reports/charts/aum_growth.png", bbox_inches="tight")
plt.close()

plt.show()
# Insight 2:
# Assets Under Management (AUM) increased steadily across major
# fund houses, reflecting growing investor participation.


# Insight 3:
# Monthly SIP inflows showed a strong upward trend, indicating
# increasing retail investor confidence in systematic investing.

fig = px.line(
    sip,
    x="month",
    y="sip_inflow_crore",
    title="Monthly SIP Inflow Trend"
)

fig.write_image("../reports/charts/sip_trend.png")

# Insight 4:
# Equity-oriented categories attracted the highest inflows during
# most periods, demonstrating investor preference for growth assets.pivot = category.pivot(
    index="category",
    columns="month",
    values="net_inflow_crore"
)

plt.figure(figsize=(15,8))

sns.heatmap(
    pivot,
    cmap="YlGnBu"
)

plt.title("Category-wise Net Inflow Heatmap")

plt.savefig("../reports/charts/category_heatmap.png", bbox_inches="tight")
plt.close()

# Insight 5:
# Young and middle-aged investors form the largest share of
# mutual fund participants.
age_counts = transactions["age_group"].value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    age_counts,
    labels=age_counts.index,
    autopct="%1.1f%%"
)

plt.title("Investor Age Group Distribution")

plt.savefig("../reports/charts/age_distribution.png", bbox_inches="tight")
plt.close()

# Insight 6:
# Older age groups tend to contribute higher SIP amounts due to
# greater earning capacity and accumulated wealth.
sip_txn = transactions[
    transactions["transaction_type"] == "SIP"
]

plt.figure(figsize=(10,6))

sns.boxplot(
    data=sip_txn,
    x="age_group",
    y="amount_inr"
)

plt.title("SIP Amount by Age Group")

plt.savefig("../reports/charts/sip_boxplot.png", bbox_inches="tight")
plt.close()

# Insight 7:
# Investor participation shows a noticeable gender imbalance,
# highlighting opportunities for broader financial inclusion.
gender = transactions["gender"].value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    gender,
    labels=gender.index,
    autopct="%1.1f%%"
)

plt.title("Gender Distribution")

plt.savefig("../reports/charts/gender_split.png", bbox_inches="tight")
plt.close()

# Insight 8:
# A few major states account for a significant portion of total
# SIP investments, indicating regional concentration.
state_sip = (
    transactions
    .groupby("state")["amount_inr"]
    .sum()
    .sort_values()
)

plt.figure(figsize=(12,8))

state_sip.plot(kind="barh")

plt.title("SIP Amount by State")

plt.savefig("../reports/charts/state_sip.png", bbox_inches="tight")
plt.close()

# Insight 9:
# T30 cities contribute the majority of investments, while B30
# cities continue to show growing participation.

tier = transactions["city_tier"].value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    tier,
    labels=tier.index,
    autopct="%1.1f%%"
)

plt.title("T30 vs B30 City Tier Distribution")

plt.savefig("../reports/charts/city_tier.png", bbox_inches="tight")
plt.close()

# Insight 10:
# Total mutual fund folios increased significantly from 2022 to
# 2025, indicating rapid expansion of the investor base.
folio["month"] = pd.to_datetime(folio["month"])

plt.figure(figsize=(12,6))

plt.plot(
    folio["month"],
    folio["total_folios_crore"]
)

plt.title("Industry Folio Growth (2022–2025)")
plt.xlabel("Month")
plt.ylabel("Total Folios (Crore)")

plt.savefig("../reports/charts/folio_growth.png", bbox_inches="tight")
plt.close()

# Insight 11:
# Financial Services, IT, and Banking sectors constitute a large
# share of portfolio allocations across equity funds.
sector = (
    portfolio
    .groupby("sector")["weight_pct"]
    .sum()
)

fig = px.pie(
    values=sector.values,
    names=sector.index,
    hole=0.5,
    title="Sector Allocation Across Equity Funds"
)

fig.write_image("../reports/charts/sector_allocation.png")
plt.figure(figsize=(10,6))

# Insight 12:
# Most schemes maintain expense ratios within the regulatory and
# industry-standard range, ensuring cost efficiency.
sns.histplot(
    performance["expense_ratio_pct"],
    bins=20
)

plt.title("Expense Ratio Distribution")

plt.savefig("../reports/charts/expense_ratio_distribution.png",
            bbox_inches="tight")
plt.close()
plt.figure(figsize=(10,6))

# Insight 13:
# The majority of funds delivered positive 3-year returns,
# reflecting favorable market performance over the period.
sns.histplot(
    performance["return_3yr_pct"],
    bins=20
)

plt.title("3-Year Return Distribution")

plt.savefig("../reports/charts/return_distribution.png",
            bbox_inches="tight")
plt.close()
plt.figure(figsize=(10,6))
# Insight 14:
# Larger funds generally tend to have lower expense ratios,
# benefiting from economies of scale.
sns.scatterplot(
    data=performance,
    x="aum_crore",
    y="expense_ratio_pct"
)

plt.title("AUM vs Expense Ratio")

plt.savefig("../reports/charts/aum_vs_expense.png",
            bbox_inches="tight")
plt.close()
plt.figure(figsize=(10,6))
# Insight 15:
# Most schemes exhibit positive Sharpe Ratios, suggesting
# favorable risk-adjusted returns.
sns.histplot(
    performance["sharpe_ratio"],
    bins=20
)

plt.title("Sharpe Ratio Distribution")

plt.savefig("../reports/charts/sharpe_ratio.png",
            bbox_inches="tight")
plt.close()
plt.figure(figsize=(10,6))
# Insight 16:
# Equity categories dominate the fund universe, reflecting
# strong investor interest in long-term capital appreciation.
fund_master["category"].value_counts().plot(
    kind="bar"
)

plt.title("Number of Funds by Category")

plt.savefig("../reports/charts/fund_category_count.png",
            bbox_inches="tight")
plt.close()

# ==================================================
# EDA CONCLUSION
# ==================================================
# The analysis highlights strong growth in India's
# mutual fund industry between 2022 and 2025.
# Rising SIP inflows, increasing folio counts,
# expanding AUM, and positive NAV trends indicate
# growing investor confidence. Demographic,
# geographic, and fund-level analyses provide
# valuable insights into investor behavior and
# industry performance.


