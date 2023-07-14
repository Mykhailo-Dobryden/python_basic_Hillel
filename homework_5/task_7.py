"""7. ** дод. Написати функцію `is_date`, що приймає 3 аргументи - день, місяць і рік.
Повернути `True`, якщо дата коректна (треба враховувати число місяця.
Наприклад 30.02 - дата не коректна, так само 31.06 або 32.07 тощо), та `False` інакше.
(можна використовувати модуль datetime)"""


def is_date(d: int, m: int, y: int) -> bool:
    """Return True in case is date is real, False - if date is wrong"""
    months = {1: 31, 2: 28, 3: 31,
              4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30,
              10: 31, 11: 30, 12: 31}  # dict of months with days

    if months.get(m) is None:
        return False
    if y < 1:  # Our calendar counting years from AD 1
        return False
    if y % 400 == 0 or (y % 4 == 0 and y % 100 > 0):  # validation for leap year
        months[2] = 29
    if d not in range(1, months[m] + 1):
        return False
    return True


def input_date() -> tuple[int, int, int]:
    """Here is parsing a str to tuple with next values of int:
    (day (d), month (m), years (y))"""
    date_str = input("Enter date in format dd.mm.yyyy: ")
    d, m, y = date_str.split(".")
    return int(d), int(m), int(y)


user_date = input_date()
day, month, year = user_date

print(is_date(day, month, year))
