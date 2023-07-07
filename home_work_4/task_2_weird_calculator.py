"""2. Програма запитує введення послідовності цілих невід'ємних чисел,
доки не буде введено 0. Як тільки буде введено 0 (нуль),
програма повинна порахувати та вивести на екран:
- кількість введених чисел (завершальний 0 не рахується)
- їхню суму
- добуток
- середнє арифметичне (крім завершального числа 0)
- Визначити значення та порядковий номер найбільшого елемента послідовності.
    Якщо найбільших елементів є кілька, виведіть порядковий номер першого з них.
    Нумерація елементів починається з 1 (однини)
- визначити кількість парних та непарних елементів у послідовності
- Визначити значення другого за величиною елемента в цій послідовності
- визначте, скільки елементів цієї послідовності дорівнюють її найбільшому елементу
"""

from task_2_calc_functions import multiply, get_odd_even, \
    find_second_largest, count_largest_nums
import statistics
import math

num_list = []

while True:
    num = int(input("Enter a positive integers or enter 0 to exit: "))
    if num == 0:
        break
    num_list.append(num)


print(num_list)
# - кількість введених чисел (завершальний 0 не рахується):
print(f"The quantity of entered numbers is: {len(num_list)}")

# їхню суму:
print(f"The sum of numbers is: {sum(num_list)}")

# - добуток:
print(f"The product of numbers is: {math.prod(num_list)}")
# print(f"The product of numbers is: {multiply(num_list)}")

# - середнє арифметичне (крім завершального числа 0):
print(f"The arithmetic mean of numbers is: {statistics.mean(num_list)}")

# - Визначити значення та порядковий номер найбільшого елемента послідовності.
print(f"Maximum value is {max(num_list)} with index {num_list.index(max(num_list)) + 1}")

# - визначити кількість парних та непарних елементів у послідовності:
odd_even_tuple = get_odd_even(num_list)
print(f"Odd = {odd_even_tuple[0]}; Even = {odd_even_tuple[1]}")

# - Визначити значення другого за величиною елемента в цій послідовності
print(f"The second highest number is {find_second_largest(num_list)}")

# - визначте, скільки елементів цієї послідовності дорівнюють її найбільшому елементу
print(f"The number of largest nums is {count_largest_nums(num_list)}")
