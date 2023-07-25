"""1. Дано два списки чисел. Порахуйте кількість чисел які міститься
як у першому списку так і у другому. (set)"""


def count_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return len(set1 | set2)


list_one = [1, 2, 3, 5, 6]
list_two = [7, 8, 3, 5, 0]

# print(set(list_one) | set(list_two))
print(count_elements(list_one, list_two))
