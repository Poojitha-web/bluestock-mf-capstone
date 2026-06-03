from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///db/bluestock_mf.db"
)

count = pd.read_sql(
    "SELECT COUNT(*) as rows FROM dim_fund",
    engine
)

print(count)