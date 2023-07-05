"""Друкувати список list_ten = [10, 20, 30, 40, 50] реверсивно - тобто.
програма має повернути [50, 40, 30, 20, 10]"""


# First Variant with .reverse() built-in method

list_ten = list(range(10, 51, 10))
list_ten.reverse()
print(list_ten)

# Second Variant with While loop

list_to_reverse = list(range(10, 51, 10))

reversed_list = []
i = len(list_to_reverse) - 1

while i >= 0:
    reversed_list.append(list_to_reverse[i])
    i -= 1

print(reversed_list)

# Third Variant with For .. In loop

list_to_reverse = list(range(10, 51, 10))

new_list = []

for elem in list_to_reverse:
    new_list.insert(0, elem)

print(new_list)
