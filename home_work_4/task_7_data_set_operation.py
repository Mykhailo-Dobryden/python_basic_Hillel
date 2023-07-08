"""7. ** Дано два списки чисел. Надрукувати:
  - числа, що містяться одночасно як у першому списку, так і в другому
  - числа, що містяться в першому, але відсутні в другому
  - тільки унікальні для першого та другого списків"""


def compare_list(list_one, list_two):
    common_in_both_list = set(list_one).intersection(set(list_two))
    uniq_for_first_list = set(list_one).difference(set(list_two))
    symmetric_differ = set(list_one).symmetric_difference(set(list_two))

    print(f"Numbers that exist in both list: {common_in_both_list}")
    print(f"Numbers that exist only in first list: {uniq_for_first_list}")
    print(f"Only uniq values of both list: {symmetric_differ}")


data_one = [2, 5, 4, 11, 10, 3, 9]
data_two = [2, 7, 6, 18, 10, 3]

compare_list(data_one, data_two)
