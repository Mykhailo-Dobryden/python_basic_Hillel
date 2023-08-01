"""3. Написати функцію яка поверне найдовше слово у рядку:
longest_word("What makes a good man") -> makes"""


def longest_word(string):
    list_strings = string.split()
    return max(list_strings, key=lambda x: len(x))


print(longest_word("What makes a good man better than woman?"))



