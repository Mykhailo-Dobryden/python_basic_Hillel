"""1. Написати функцію `is_prime`, що приймає 1 аргумент - число від 0 до 1000,
і повертає `True`, якщо воно просте, і `False` - інакше.
(Прості числа - ті які діляться без залишку тільки на себе або 1,
наприклад 2, 3, 5, 7, 11 ...)"""


def is_prime(num: int):
    """Return True if number is prime number, else return False"""
    if num < 0 or num > 1000:
        return str(f"Number {num} is out of required range")
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


simple_num = int(input("Enter number from 0 to 1000: "))
print(is_prime(simple_num))
