import requests
import json
from datetime import datetime
import os

def extract_brewery_data():
    # url = "https://api.openbrewerydb.org/breweries"
    url = "https://api.openbrewerydb.org/v1/breweries"
    response = requests.get(url)
    data = response.json()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("data/bronze", exist_ok=True)
    with open(f"data/bronze/breweries_{timestamp}.json", "w") as f:
        json.dump(data, f)