"""3. Пароль, що вводиться користувачем, повинен відповідати вимогам,

  1. Як мінімум 1 символ від a-z
  2. Як мінімум 1 символ від A-Z
  3. Щонайменше 1 символ від 0-9
  4. Як мінімум 1 символ із $#@-+=
  5. Мінімальна довжина пароля 8 символів.

  Програма приймає на введення рядок, якщо пароль неправильний - пише якій саме
  вимозі не відповідає і запитує знову, якщо правильний - пише 'Password is correct'."""

import re


def is_lowercase(s: str) -> bool | str:
    """
    Check if given strings contains at least 1 lowercase letter [a-z].
    Args:
        s (str): string to be checked

    Returns:
        True if contains lowercase letter, otherwise returns descriptive string.
    """
    match = re.search(r'[a-z]+', s)
    if not match:
        return "Password must have at least 1 lowercase letter "
    return True


def is_uppercase(s: str) -> bool | str:
    """
    Check if given strings contains at least 1 uppercase letter [A-Z].
    Args:
        s (str): string to be checked

    Returns:
        True if contains uppercase letter, otherwise returns descriptive string.
    """
    match = re.search(r'[A-Z]+', s)
    if not match:
        return "Password must have at least 1 uppercase letter "
    return True


def is_digit(s: str) -> bool | str:
    """
    Check if given strings contains at least 1 digit [0-9].
    Args:
        s (str): string to be checked

    Returns:
        True if contains digit, otherwise returns descriptive string.
    """
    match = re.search(r'\d+', s)
    if not match:
        return "Password must have at least 1 digit"
    return True


def is_special_character(s: str) -> bool | str:
    """
    Check if given strings contains at least 1 special characters [$#@-+=].
    Args:
        s (str): string to be checked

    Returns:
        True if contains digit, otherwise returns descriptive string.
    """
    match = re.search(r'[$#@\-+=]+', s)
    if not match:
        return "Password must have at least 1 special character: $#@-+="
    return True


def check_lenght(s: str) -> bool | str:
    """
    Check if given string has length not less than 8 symbols.
    Args:
        s (str): string to be checked

    Returns:
        True if length >= 8, otherwise returns descriptive string.
    """
    if len(s) < 8:
        return "The length of password should be not less than 8 symbols"
    return True


def user_input(prompt: str) -> str:
    """
    Prompt the user for input and return the entered text after stripping any leading/trailing whitespace.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        str: The user-entered text after stripping whitespace.
    """
    password = input(prompt)
    return password.strip()


# The list of function needed for password validation:
PASS_VALIDATION = [
    is_lowercase,
    is_uppercase,
    is_digit,
    is_special_character,
    check_lenght
]

# --------------client code:-------------
if __name__ == '__main__':

    while True:
        user_password = input("Enter password: ")
        check_points = 0
        for v in PASS_VALIDATION:
            result = v(user_password)
            if result == True:
                check_points += 1
            else:
                print(result)
        if check_points == 5:
            print("Password is correct")
            break
