import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///db/bluestock_mf.db")

tables = [
    "dim_fund",
    "fact_nav",
    "fact_aum",
    "fact_performance",
    "fact_transactions"
]

for table in tables:
    result = pd.read_sql(
        f"SELECT COUNT(*) as rows FROM {table}",
        engine
    )

    print(table)
    print(result)
    print("-" * 40)