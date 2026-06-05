import pandas as pd
import numpy as np
import os
import plotly.express as px

print("Current Directory:", os.getcwd())

nav = pd.read_excel("../Data/raw/02_nav_history.xlsx")

performance = pd.read_excel("../Data/raw/07_scheme_performance.xlsx")

benchmark = pd.read_excel("../Data/raw/10_benchmark_indices.xlsx")
print(nav.shape)

print(performance.shape)
print(benchmark.shape)
# -------------------------------
# Daily Returns
# -------------------------------

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
       .pct_change()
)

print("\nDaily Return Summary")
print(nav["daily_return"].describe())
# -------------------------------
# CAGR
# -------------------------------

cagr_data = []

for code in nav["amfi_code"].unique():

    temp = nav[
        nav["amfi_code"] == code
    ].sort_values("date")

    start_nav = temp["nav"].iloc[0]
    end_nav = temp["nav"].iloc[-1]

    years = (
        (temp["date"].max() -
         temp["date"].min()).days
        / 365
    )

    cagr = (
        (end_nav / start_nav)
        ** (1 / years)
    ) - 1

    cagr_data.append(
        [code, cagr]
    )

cagr_df = pd.DataFrame(
    cagr_data,
    columns=["amfi_code", "cagr"]
)

print("\nTop CAGR Funds")
print(
    cagr_df.sort_values(
        "cagr",
        ascending=False
    ).head()
)

# -------------------------------
# Sharpe Ratio
# -------------------------------

import numpy as np

rf = 0.065

sharpe = (
    nav.groupby("amfi_code")
       ["daily_return"]
       .apply(
           lambda x:
           ((x.mean()*252)-rf)
           /
           (x.std()*np.sqrt(252))
       )
)

sharpe_df = sharpe.reset_index()

sharpe_df.columns = [
    "amfi_code",
    "sharpe_ratio"
]

print("\nTop Sharpe Ratio Funds")
print(
    sharpe_df.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head()
)

# -------------------------------
# Sortino Ratio
# -------------------------------

def sortino(x):

    downside = x[x < 0]

    if len(downside) == 0:
        return np.nan

    return (
        ((x.mean()*252)-rf)
        /
        (downside.std()*np.sqrt(252))
    )

sortino_df = (
    nav.groupby("amfi_code")
       ["daily_return"]
       .apply(sortino)
       .reset_index()
)

sortino_df.columns = [
    "amfi_code",
    "sortino_ratio"
]

print("\nTop Sortino Ratio Funds")
print(
    sortino_df.sort_values(
        "sortino_ratio",
        ascending=False
    ).head()
)

# -------------------------------
# Maximum Drawdown
# -------------------------------

drawdown_list = []

for code in nav["amfi_code"].unique():

    temp = nav[
        nav["amfi_code"] == code
    ].copy()

    temp["running_max"] = (
        temp["nav"].cummax()
    )

    temp["drawdown"] = (
        temp["nav"]
        /
        temp["running_max"]
        - 1
    )

    max_dd = temp["drawdown"].min()

    drawdown_list.append(
        [code, max_dd]
    )

drawdown_df = pd.DataFrame(
    drawdown_list,
    columns=[
        "amfi_code",
        "max_drawdown"
    ]
)

print("\nWorst Drawdowns")
print(
    drawdown_df.sort_values(
        "max_drawdown"
    ).head()
)

print("\nBenchmark Names")
print(
    benchmark["index_name"]
    .unique()
)

from scipy.stats import linregress

# NIFTY100 benchmark
nifty = benchmark[
    benchmark["index_name"] == "NIFTY100"
].copy()

nifty["date"] = pd.to_datetime(nifty["date"])
nifty = nifty.sort_values("date")

nifty["benchmark_return"] = (
    nifty["close_value"]
    .pct_change()
)

alpha_beta = []

for code in nav["amfi_code"].unique():

    fund = nav[
        nav["amfi_code"] == code
    ][["date", "daily_return"]]

    merged = pd.merge(
        fund,
        nifty[["date", "benchmark_return"]],
        on="date",
        how="inner"
    ).dropna()

    if len(merged) > 30:

        slope, intercept, r, p, se = linregress(
            merged["benchmark_return"],
            merged["daily_return"]
        )

        beta = slope
        alpha = intercept * 252

        alpha_beta.append(
            [code, alpha, beta]
        )

alpha_beta_df = pd.DataFrame(
    alpha_beta,
    columns=[
        "amfi_code",
        "alpha",
        "beta"
    ]
)

print("\nTop Alpha Funds")
print(
    alpha_beta_df.sort_values(
        "alpha",
        ascending=False
    ).head()
)

alpha_beta_df.to_csv(
    "../outputs/alpha_beta.csv",
    index=False
)

scorecard = (
    cagr_df
    .merge(sharpe_df,on="amfi_code")
    .merge(alpha_beta_df,on="amfi_code")
    .merge(drawdown_df,on="amfi_code")
)

scorecard["return_rank"] = \
scorecard["cagr"].rank(
    ascending=False
)

scorecard["sharpe_rank"] = \
scorecard["sharpe_ratio"].rank(
    ascending=False
)

scorecard["alpha_rank"] = \
scorecard["alpha"].rank(
    ascending=False
)

scorecard["dd_rank"] = \
scorecard["max_drawdown"].rank(
    ascending=False
)

max_rank = len(scorecard)

scorecard["score"] = (
    (max_rank-scorecard["return_rank"])
    *0.30
    +
    (max_rank-scorecard["sharpe_rank"])
    *0.25
    +
    (max_rank-scorecard["alpha_rank"])
    *0.20
    +
    (max_rank-scorecard["dd_rank"])
    *0.10
)

scorecard["score"] = (
    scorecard["score"]
    /
    scorecard["score"].max()
)*100

print("\nTop Funds Scorecard")
print(
    scorecard.sort_values(
        "score",
        ascending=False
    ).head()
)

scorecard.to_csv(
    "../outputs/fund_scorecard.csv",
    index=False
)

top5 = (
    scorecard
    .sort_values(
        "score",
        ascending=False
    )
    .head(5)
)["amfi_code"]

chart_data = nav[
    nav["amfi_code"].isin(top5)
]

fig = px.line(
    chart_data,
    x="date",
    y="nav",
    color="amfi_code",
    title="Top 5 Funds Benchmark Comparison"
)

fig.write_image(
    "../reports/charts/benchmark_comparison.png"
)

print(
    "\nBenchmark chart saved"
)