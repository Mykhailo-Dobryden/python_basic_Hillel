"""2. Написати програму яка форматуватиме номер телефону до єдиного вигляду.
  На введення програма приймає рядок введеного телефонного номера, наприклад:

  063-999-99-99 повертає (+38) 063 999-99-99
  063 999-99-99 повертає (+38) 063 999-99-99
  063-99999-99 повертає (+38) 063 999-99-99
  +3806399-999-99 повертає (+38) 063 999-99-99
  380639999999 повертає (+38) 063 999-99-99
  38(0 63) 123 45 67 --> (+38) 063 123-45-67
  Якщо щось не так із номером - пише 'Failed to recognize number'."""

import re


PATTERN = re.compile(r"^\+?3?8?\(?[ -]*(0)[ -]*(\d)[ -]*(\d)\)?[ -]*(\d)[ -]*(\d)[ -]*(\d)[ -]*(\d)[ -]*(\d)[ -]*(\d)[ -]*(\d)[ -]*$")


def user_input(prompt) -> str:
    """
    Prompt the user for input and return the entered text after stripping any leading/trailing whitespace.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        str: The user-entered text after stripping whitespace.
    """
    phone_number = input(prompt)
    return phone_number.strip()


def format_phone_number(phone: str) -> str:
    """
    Format a phone number to a unified pattern.

    Args:
        phone (str): The input phone number to format.

    Returns:
        str: The formatted phone number in the pattern "(+38) 063 999-99-99".

    Raises:
        ValueError: If the provided phone number doesn't match the expected pattern.
    """
    match = PATTERN.search(phone)
    if not match:
        raise ValueError("Failed to recognize number")

    formatted_number = re.sub(PATTERN, r"(+38) \1\2\3 \4\5\6-\7\8-\9\10", phone)
    return formatted_number


def main():
    """
    Main function to format a phone number entered by the user and print the formatted result.
    """
    phone = user_input("Enter a phone number: ")
    formatted_number = format_phone_number(phone)
    print(formatted_number)


# -----------------------client code:-------------------
if __name__ == '__main__':

    main()




