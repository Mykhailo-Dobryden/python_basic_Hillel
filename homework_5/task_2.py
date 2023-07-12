"""2. Написати програму яка поверне кількість введених користувачем слів
та загальну кількість символів."""


def get_user_input():
    return input("Enter a sentence: ")


def get_str_analysis(data: str):
    """Return a tuple, where 1st value - a number of words,
    2nd - a number of symbols"""
    words_num = data.split()
    symbols_num = data.replace(" ", "")
    return len(words_num), len(symbols_num)


user_input = get_user_input()
str_report = get_str_analysis(user_input)
words_symbols, symbols_count = str_report
print(f"The words are: {words_symbols}")
print(f"The symbols are: {symbols_count}")
