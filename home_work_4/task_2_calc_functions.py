
def get_quantity_nums(data_list: list) -> int:
    """Return the quantity of numbers is the list"""
    return len(data_list)


def multiply(data_list: list) -> int:
    """Return the product of numbers in the list"""
    result = 1
    for i in data_list:
        result *= i
    return result


def get_odd_even(data_list: list) -> tuple:
    """Return a tuple, where first value is a quantity of odd numbers;
    and second value is a quantity of even numbers"""
    odd, even = 0, 0
    for i in data_list:
        if i % 2 == 1:
            odd += 1
        else:
            even += 1
    return odd, even


def find_second_largest(data_list: list) -> int:
    """Return the second-highest value"""
    new_list = sorted(set(data_list))
    return new_list[-2]


def count_largest_nums(data_list: list) -> int:
    largest = max(data_list)
    quantity_largest = data_list.count(largest)
    return quantity_largest


if __name__ == '__main__':
    print(get_quantity_nums([2, 3, 4, 5]))

    print(multiply([1, 2, 3, 99, 99, 3, 5, 6]))

    print(get_odd_even([1, 2, 3, 99, 3, 5, 6]))
    print(find_second_largest([1, 6, 2, 3, 99, 99, 3, 5, 6]))

    print(count_largest_nums([1, 6, 2, 3, 99, 99, 3, 5, 6]))

