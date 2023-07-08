"""Дано два цілих числа 'A' і 'В'. Виведіть усі числа від `A` до `B` включно,
в порядку зростання, якщо `A < B`, або в порядку зменшення в іншому випадку."""


def get_ab_range(a: int, b: int):
    if a < b:
        return ', '.join(map(str, range(a, b + 1)))
    else:
        return ', '.join(map(str, range(a, b - 1, -1)))


number_a = int(input("Enter number A: "))
number_b = int(input("Enter number B: "))

print(get_ab_range(number_a, number_b))

# print(', '.join([str(item) for item in range(1, 10+1)]))
