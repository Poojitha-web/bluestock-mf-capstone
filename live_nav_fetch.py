import requests
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    print(f"\nFetching {name} ({code})")

    try:

        response = requests.get(url, timeout=20)

        print("Status Code:", response.status_code)

        if response.status_code != 200:
            print("Failed")
            continue

        data = response.json()

        if "data" not in data:
            print("No NAV data found")
            continue

        df = pd.DataFrame(data["data"])

        df.to_csv(
            f"data/raw/{name}.csv",
            index=False
        )

        print(f"Saved {name}")

    except Exception as e:
        print(f"Error for {name}: {e}")