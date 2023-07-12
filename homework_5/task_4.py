"""4. Даний перелік випадкових цілих чисел. Замініть усі непарні
числа списку нулями. І виведете їхню кількість."""


def replace_odd_nums(data: list) -> tuple:
    """Return a tuple with two values: list with replaced odd nums by 0
    and total count of replacement"""
    odd_count = 0
    for index, num in enumerate(data):
        if num % 2 == 1:
            data[index] = 0
            odd_count += 1
    return data, odd_count


random_nums = [1, 10, 3, 8, 3, 5, 6, 8, 13, 45, 22]
replaced_nums, zero_count = replace_odd_nums(random_nums)

print(f"New list with replaced odd numbers: {replaced_nums}")
print(f"Total number replaced numbers: {zero_count}")
