Mutual Fund Analytics Capstone Project

 Overview

The Mutual Fund Analytics Capstone Project is an end-to-end data analytics solution designed to analyze mutual fund performance, investor behavior, industry growth trends, and portfolio risk. The project integrates multiple datasets and transforms raw financial data into meaningful insights using Python, SQLite, SQL, and Power BI.

The objective of this project is to demonstrate the complete analytics lifecycle including data ingestion, data cleaning, database management, exploratory data analysis (EDA), performance analytics, advanced analytics, and dashboard development.

---

Business Problem

Investors and fund managers require reliable insights into mutual fund performance, risk metrics, SIP trends, investor demographics, and industry growth. Raw mutual fund data is often fragmented across multiple sources, making analysis difficult.

This project addresses the problem by creating a centralized analytics platform capable of:

* Tracking mutual fund performance
* Measuring risk-adjusted returns
* Understanding investor behavior
* Monitoring industry growth
* Supporting investment decision-making through interactive dashboards

---

 Project Objectives

* Build an automated ETL pipeline for mutual fund datasets.
* Clean and validate raw financial data.
* Store structured data in a SQLite database.
* Perform Exploratory Data Analysis (EDA).
* Calculate key performance and risk metrics.
* Develop advanced analytics models.
* Create interactive Power BI dashboards.
* Generate actionable investment insights.

---

 Datasets Used

| Dataset               | Description                                 |
| --------------------- | ------------------------------------------- |
| Fund Master           | Mutual fund scheme details                  |
| NAV History           | Daily Net Asset Value history               |
| AUM Data              | Assets Under Management by fund house       |
| Monthly SIP Inflows   | Monthly SIP contribution data               |
| Category Inflows      | Fund category-wise inflows                  |
| Industry Folio Count  | Industry folio growth statistics            |
| Scheme Performance    | Historical return metrics                   |
| Investor Transactions | Investor-level transaction data             |
| Portfolio Holdings    | Portfolio composition and sector allocation |
| Benchmark Indices     | Nifty and benchmark index data              |

---

 Technology Stack

 Programming Languages

* Python
* SQL

 Python Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SciPy
* SQLite3

 Database

* SQLite

 Visualization

* Power BI
* Plotly
* Matplotlib
* Seaborn

 Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

 Project Architecture

Raw Data
→ Data Cleaning
→ Data Validation
→ Data Transformation
→ SQLite Database
→ EDA Analysis
→ Performance Analytics
→ Advanced Analytics
→ Power BI Dashboard
→ Business Insights

---

 ETL Pipeline

 Extract

Raw mutual fund datasets were collected from multiple sources.

 Transform

The following transformations were performed:

* Missing value handling
* Duplicate removal
* Data type correction
* Date formatting
* Data validation
* Data consistency checks

 Load

Cleaned datasets were loaded into SQLite database tables for analytics and reporting.

---

 Database Design

 Tables Created

 Dimension Table

* dim_fund

 Fact Tables

* fact_nav
* fact_aum
* fact_performance
* fact_transactions

The database stores thousands of records and supports analytical queries efficiently.

---

 Exploratory Data Analysis (EDA)

The EDA phase focused on identifying trends, growth patterns, and investor behavior.

 Analyses Performed

 1. NAV Trend Analysis

* Daily NAV trends across all mutual fund schemes
* Identification of market growth periods and corrections

 2. AUM Growth Analysis

* Fund house-wise AUM comparison
* Industry dominance analysis

 3. SIP Inflow Analysis

* Monthly SIP contribution trends
* Peak inflow identification

 4. Category Inflow Analysis

* Net inflows across fund categories
* Heatmap visualization

 5. Investor Demographics

* Age group analysis
* Gender distribution
* Investment patterns

 6. Geographic Distribution

* State-wise investment analysis
* T30 vs B30 city comparison

 7. Folio Growth Analysis

* Industry growth tracking
* Investor participation trends

---

 Performance Analytics

Performance metrics were calculated to evaluate mutual fund efficiency and risk-adjusted returns.

 Daily Returns

Calculated using:

Daily\ Return=\frac{NAV_t}{NAV_{t-1}}-1

 CAGR

Calculated using:

CAGR=\left(\frac{NAV_{end}}{NAV_{start}}\right)^{\frac{1}{n}}-1

 Sharpe Ratio

Calculated using:

Sharpe=\frac{R_p-R_f}{\sigma_p}\sqrt{252}

 Sortino Ratio

Calculated using downside volatility only.

 Alpha and Beta

Computed using benchmark regression against Nifty 100 returns.

Maximum Drawdown

Measured maximum decline from historical peak NAV.

 Fund Scorecard

Composite ranking based on:

* 30% CAGR Rank
* 25% Sharpe Rank
* 20% Alpha Rank
* 15% Expense Ratio Rank
* 10% Drawdown Rank

---

 Advanced Analytics

 Value at Risk (VaR)

Estimated potential downside risk at 95% confidence level.

 Cohort Analysis

Investor segmentation based on:

* Age Group
* City Tier

 Fund Recommendation Engine

Top-performing funds identified using:

* Historical returns
* Risk-adjusted performance
* Fund rankings

---

 Power BI Dashboard

The project includes a four-page interactive dashboard.

 Page 1 – Executive Dashboard

* Total Funds
* Total AUM
* Average NAV
* Industry KPIs

 Page 2 – Performance Analytics

* Risk vs Return Analysis
* Alpha Beta Analysis
* Drawdown Analysis

 Page 3 – Investor Analytics

* Age Distribution
* Gender Split
* Geographic Distribution

 Page 4 – Industry Analytics

* SIP Trends
* Category Inflows
* Folio Growth

 Dashboard Features

* Interactive slicers
* Dynamic filtering
* KPI cards
* Trend analysis
* Cross-page navigation

---

 Key Findings

1. Small Cap Funds delivered the highest long-term returns.
2. SBI Mutual Fund maintained industry-leading AUM.
3. SIP inflows demonstrated strong year-over-year growth.
4. Investors aged 26–35 contributed the highest investment volume.
5. T30 cities generated significantly higher investments than B30 cities.
6. Equity categories attracted the highest net inflows.
7. Industry folio counts nearly doubled during the analysis period.
8. Fund 148567 achieved the highest Sharpe Ratio.
9. Small Cap Funds dominated the recommendation engine.
10. Risk-adjusted performance varied significantly across fund categories.

---

 Future Enhancements

* Streamlit Web Application
* Real-Time NAV Monitoring
* Automated Email Reporting
* Monte Carlo Simulation
* Portfolio Optimization
* Markowitz Efficient Frontier Analysis

---

 Folder Structure

```text
mutual_fund_analytics/
│
├── Data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA_Analysis.py
│   ├── Performance_Analytics.py
│   └── Advanced_Analytics.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── Final_Report.pdf
│   ├── Presentation.pptx
│   └── charts/
│
├── README.md
└── requirements.txt
```

---

Author: Kurapati Poojitha

Role: Data Analytics Intern

 Skills Demonstrated

* Data Cleaning
* ETL Pipelines
* SQL & SQLite
* Data Visualization
* Exploratory Data Analysis
* Financial Analytics
* Risk Analysis
* Power BI Dashboarding
* Business Intelligence

---

 License

This project was developed as part of a Data Analytics Internship Capstone Project for educational and portfolio purposes.
