# scripts/extract.py

import requests
import json

def extract(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    url = "https://api.publicapis.org/entries"
    data = extract(url)
    with open("../data/raw_data.json", "w") as f:
        json.dump(data, f)
    print("Data extracted successfully.")