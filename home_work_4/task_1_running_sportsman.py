"""1. Першого дня спортсмен пробіг `x` кілометрів, а потім він
щодня збільшував пробіг на 10% від попереднього значення. За цим числом `y`
визначте номер дня, на який відстань спортсмена складе не менше `y` кілометрів.
Програма отримує на вхід числа `x` та `y` і має вивести одне число - номер дня."""


def return_marathon_day(a: int, b: int) -> int:
    """a - is distance for first day, b - distance for desired day"""
    day = 1
    while b > a:
        b *= 0.9
        day += 1
    return day


def user_input(prompt: str = "Enter a number: ") -> int:
    return int(input(prompt))


number_x = user_input("Enter a number x: ")
number_y = user_input("Enter a number y: ")

print(return_marathon_day(number_x, number_y))

