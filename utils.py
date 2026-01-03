from datetime import datetime

def parse_date(date_str: str) -> str:
    """
    Validates and returns a date string in YYYY-MM-DD format.
    Raises ValueError if invalid.
    """
    try:
        parsed = datetime.strptime(date_str, "%Y-%m-%d")
        return parsed.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")


def parse_time(time_str: str) -> int:
    """
    Converts HH:MM into minutes since midnight.
    """
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes
