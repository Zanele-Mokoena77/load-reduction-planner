import json
from utils import parse_time

DAY_START = 0
DAY_END = 24 * 60

def load_data(filepath: str) -> dict:
    with open(filepath, "r") as filepath:
        data = json.load(file)
    return data

def get_outages(data: dict, suburb: str) -> list:
   if suburb not in data:
        raise ValueError(f"Suburb {suburb} not found in data")

    resp = data.get(suburb, {}).get(date, [])
    return resp
        