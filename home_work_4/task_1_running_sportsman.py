"""1. Першого дня спортсмен пробіг `x` кілометрів, а потім він
щодня збільшував пробіг на 10% від попереднього значення. За цим числом `y`
визначте номер дня, на який відстань спортсмена складе не менше `y` кілометрів.
Програма отримує на вхід числа `x` та `y` і має вивести одне число - номер дня."""


def return_marathon_day(a: float, b: float) -> int:
    """a - is distance for first day, b - distance for desired day"""
    distance = a
    day = 1
    while distance < b:
        distance += distance * 0.1
        day += 1
    return day


def user_input(prompt: str = "Enter a number: ") -> float:
    return float(input(prompt))


number_x = user_input("Enter a number x: ")
number_y = user_input("Enter a number y: ")

num_of_day = return_marathon_day(number_x, number_y)

print(f"The day number when the distance will be not less than {number_y} is: {num_of_day}")
