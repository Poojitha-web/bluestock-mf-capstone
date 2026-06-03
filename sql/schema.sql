CREATE TABLE dim_fund (
amfi_code TEXT PRIMARY KEY,
fund_house TEXT,
scheme_name TEXT,
category TEXT,
sub_category TEXT
);

CREATE TABLE dim_date (
date_id DATE PRIMARY KEY,
year INTEGER,
month INTEGER,
day INTEGER
);

CREATE TABLE fact_nav (
amfi_code TEXT,
date DATE,
nav REAL,
FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
investor_id TEXT,
amfi_code TEXT,
transaction_date DATE,
amount_inr REAL,
FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (
amfi_code TEXT,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,
sharpe_ratio REAL,
FOREIGN KEY(amfi_code)
REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
fund_house TEXT,
aum_crore REAL
);
