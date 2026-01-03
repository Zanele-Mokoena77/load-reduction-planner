from scheduler import load_data, get_outages, calculate_safe_windows
from utils import parse_date

DATA_PATH = "data/loadreduction.json"

def format_time(minutes: int) -> str:
    """
    Converts minutes since midnight into HH:MM format.
    """
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours:02d}:{minutes:02d}"


def main():

    suburb = input("Enter suburb: ").strip()
    date_input = input("Enter date (YYYY-MM-DD): ").strip()

    try:
        date = parse_date(date_input)
        data = load_data(DATA_PATH)
        outages = get_outages(data, suburb, date)


        if not outages:
            print("No outages scheduled for this suburb on this date.")
            return


        print("\nLoad-reduction times:")
        for start,end in outages:
            print(f"{start} - {end}")


        safe_windows = calculate_safe_windows(outages)


        print("\nSafe windows for load-reduction:")
        for start, end in safe_windows:
            print(f"{format_time(start)} - {format_time(end)}")
    
    
    except ValueError as error:
        print(f"Error: {error}")



if __name__ == "__main__":
    main()

    