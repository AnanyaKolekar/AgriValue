import os
import time
import requests
import pandas as pd 

API_KEY = os.environ["CEDA_API_KEY"]

URL = "https://api.ceda.ashoka.edu.in/v1/agmarknet/prices"

crops = {
    2: "Paddy",
    4: "Maize",
    5: "Jowar",
    10: "Groundnut",
    30: "Ragi"
}

districts = list(range(555, 585))

all_data = []

for crop_id, crop_name in crops.items():

    print(f"\nDownloading {crop_name}...")

    for i in range(0, len(districts), 5):

        district_batch = districts[i:i + 5]

        payload = {
            "commodity_id": crop_id,
            "state_id": 29,
            "district_id": district_batch,
            "from_date": "2019-01-01",
            "to_date": "2025-12-31"
        }

        try:
            response = requests.post(
                URL,
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                },
                json=payload,
                timeout=90
            )

            if response.status_code != 200:
                print(f"  Batch {district_batch}: Error {response.status_code}")
                continue

            data = response.json()["output"]["data"]

            for row in data:
                row["crop"] = crop_name

            all_data.extend(data)

            print(
                f"  Districts {district_batch}: "
                f"{len(data)} records"
            )

        except Exception as e:
            print(f"  Batch {district_batch}: {e}")

        time.sleep(1)


df = pd.DataFrame(all_data)

if df.empty:
    print("\nNo data downloaded.")
else:
    df["date"] = pd.to_datetime(df["date"])

    df = df.drop_duplicates(
        subset=[
            "date",
            "commodity_id",
            "census_state_id",
            "census_district_id",
            "market_id"
        ]
    )

    df = df.sort_values(["crop", "date"])

    df.to_csv(
        "data/raw/agri_value_karnataka.csv",
        index=False
    )

    print("\nDownload complete!")
    print("Records:", len(df))
    print("Markets:", df["market_id"].nunique())
    print("\nRecords by crop:")
    print(df["crop"].value_counts())
    print("\nSaved to: data/raw/agri_value_karnataka.csv")