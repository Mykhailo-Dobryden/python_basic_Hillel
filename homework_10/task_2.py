"""2. Написати функцію, яка визначить, чи є введений текст паліндромом
(той який читається однаково з будь-якого боку), приклад:
Шалаш, зараз, Дід, Піп, 13231
Паліндром — і ні морд, ні лап"""


def is_palindrome(text):
    """Returns true is text is palindrome"""
    cleaned_text = ''.join([i for i in text.lower() if i.isalnum()])  # cleans from non-alpha-numeric symbols
    return cleaned_text == cleaned_text[::-1]


if __name__ == '__main__':

    user_input = input("Enter text for checking: ")
    if is_palindrome(user_input) is True:
        print(f"\"{user_input}\": is palindrome")
    else:
        print(f"\"{user_input}\": is not palindrome")



