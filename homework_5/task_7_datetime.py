from datetime import datetime


def is_date(d, m, y) -> bool:
    """This function create a date object. If entered data is correct, constructor
    creates date object and returns True, otherwise returns False"""
    try:
        datetime(y, m, d)
        return True
    except ValueError:
        return False


def input_date() -> tuple:
    """Here is parsing a str to tuple with next values of int:
    (day (d), month (m), years (y))"""
    date_str = input("Enter date in format dd.mm.yyyy: ")
    d, m, y = date_str.split(".")
    return int(d), int(m), int(y)


user_date = input_date()
day, month, year = user_date

print(is_date(day, month, year))
