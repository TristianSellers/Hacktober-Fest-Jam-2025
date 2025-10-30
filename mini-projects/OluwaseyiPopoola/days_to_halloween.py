from datetime import datetime

def main():
    days = days_to_halloween()
    print(f"There are {days} days until Halloween!")


def days_to_halloween():
    today = datetime.now()
    current_year = today.year
    halloween_date = datetime(current_year, 10, 31)

    # If Halloween has already passed this year, calculate for next year
    if today > halloween_date:
        halloween_date = datetime(current_year + 1, 10, 31)

    delta = halloween_date - today
    return delta.days

if __name__ == "__main__":
    main()


