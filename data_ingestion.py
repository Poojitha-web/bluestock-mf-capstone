import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")

csv_files = raw_path.glob("*.csv")

for file in csv_files:

    print("\n" + "="*80)
    print("Dataset:", file.name)

    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file.name}: {e}")