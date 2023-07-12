"""5. Написати функцію square, що приймає 1 аргумент - сторону квадрата,
і повертає 3 значення (за допомогою кортежу):
периметр квадрата, площа квадрата та діагональ квадрата."""


def get_square_info(s: float) -> tuple:
    """Return: perimeter (p), area (a) and diagonal (d) of square with given side (s)"""
    p = s * 4
    a = s ** 2
    d = 2 ** 0.5 * s
    return p, a, round(d, 2)


def user_input():
    return float(input("Give us a size of square's side: "))


input_param = user_input()
perimetr, area, diagonal = get_square_info(input_param)

print(f"Perimetr: {perimetr}")
print(f"Area: {area}")
print(f"Diagonal: {diagonal}")
