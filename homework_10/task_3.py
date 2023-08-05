"""
3. Написати функцію яка зрушить отриманий список на N елементів вправо або вліво,
аргументи, що приймаються — список і натуральне число(якщо негативне зрушуємо вліво, позитивне — вправо).
"""


# 1st variant:
def shift_list(elem: list, n: int):
    data = elem.copy()
    if n > 0:
        n = n % len(data)
        return data[-n:] + data[:-n]
    if n < 0:
        n = -n % len(data)
        return data[n:] + data[:n]
    else:
        return data


#  2nd variant:
def rotate_list(data: list, n: int):
    d = data.copy()
    if n > 0:
        for _ in range(n):
            d.insert(0, d.pop(len(d)-1))
    if n < 0:
        for _ in range(abs(n)):
            d.append(d.pop(0))
    else:
        return d
    return d


if __name__ == '__main__':
    elements = [1, 2, 3, 4, 5, 6, 7]
    shifted_list = shift_list(elements, 7)
    print(shifted_list)
    rotated_list = rotate_list(elements, 9)
    print(rotated_list)
