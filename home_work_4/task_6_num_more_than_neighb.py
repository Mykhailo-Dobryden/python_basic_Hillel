"""6. * Даний список чисел. Визначте, скільки в цьому списку елементів,
які більше двох своїх сусідів (ліворуч і праворуч),
та виведіть кількість таких елементів. Крайні елементи списку ніколи не враховуються,
оскільки вони мають недостатньо сусідів."""


def get_larger(num_list: list) -> int:
    """Return count of elements which are larger than value of their neighbours"""
    count = 0
    for i in range(1, len(num_list) - 1):
        if num_list[i - 1] < num_list[i] > num_list[i + 1]:
            count += 1
    return count


some_numbers = [600, 3, 13, 100, 60, 15, 15, 9, 5, 3, 6]
print(get_larger(some_numbers))
