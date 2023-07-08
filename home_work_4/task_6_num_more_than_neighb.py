"""6. * Даний список чисел. Визначте, скільки в цьому списку елементів,
які більше двох своїх сусідів (ліворуч і праворуч),
та виведіть кількість таких елементів. Крайні елементи списку ніколи не враховуються,
оскільки вони мають недостатньо сусідів."""


def get_larger(num_list: list) -> int:
    """Return count of elements which are larger than value of their neighbours"""
    count = 0
    for num in num_list:
        index = num_list.index(num)
        if index == 0 or index == len(num_list) - 1:
            continue
        elif num_list[index - 1] < num > num_list[index + 1]:
            count += 1
        else:
            continue
    return count


some_numbers = [600, 3, 13, 100, 60, 100, 15, 15, 9, 5, 10, 3, 6]
print(get_larger(some_numbers))
