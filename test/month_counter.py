def get_days_in_month(month):
    if month == 1:
        return 31
    elif month == 2:
        return 28  # Not accounting for leap years
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31
    else:
        return "Invalid month number"

def main():
    month = int(input("Enter the number of the month (1-12): "))
    days = get_days_in_month(month)

    if month == 31:
        print(f"The number of days in month {month} is {days}")