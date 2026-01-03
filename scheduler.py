import json
from utils import parse_time

DAY_START = 0
DAY_END = 24 * 60

def load_data(filepath: str) -> dict:
    with open(filepath, "r") as file:
        data = json.load(file)
        return data

def get_outages(data: dict, suburb: str, date: str) -> list:
    if suburb not in data:
        raise ValueError(f"Suburb {suburb} not found in data")

    resp = data.get(suburb, {}).get(date, [])
    return resp


def calculate_safe_windows(outages: list) -> list:

    safe_windows = []
    current_start = DAY_START

    for start, end in outages:
        outage_start = parse_time(start)
        outage_end = parse_time(end)

        if outage_start > current_start:
            safe_windows.append([current_start, outage_start])

        current_start = outage_end

    
    if current_start < DAY_END:
        safe_windows.append([current_start, DAY_END])


    return safe_windows


        