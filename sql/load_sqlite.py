import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///db/bluestock_mf.db"
)

fund_master = pd.read_excel(
    "Data/raw/01_fund_master.xlsx"
)

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("Loaded successfully")