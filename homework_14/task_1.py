"""1. Формат українських номерів: ВН1010НС чи АА1010АА
На введення програма отримує рядок, у відповідь має повернути чи є рядок автомобільним номером чи ні.
Повинна повернути регіон (має знати регіони 2004 та 2013 рр.)
Повинна однаково сприймати AI – англійський та АІ – український варіанти.
(Для BI, AI, IA і т.д.)
"""
import csv
import re


# Regular expression pattern for Ukrainian vehicle registration number
PATTERN = r"(?P<prefix>[А-Я]{2})\s*\d{4}\s*[А-Я]{2}"

# Characters for translation between English and Ukrainian alphabets
LATIN_CHARS = "ABEIKMHOPCTX"
CYRILLIC_CHARS = "АВЕІКМНОРСТХ"


def is_english(s: str) -> bool:
    """
    Check if a given string consists only of English letters.

    Args:
        s (str): The string to be checked.

    Returns:
        bool: True if the string consists only of English letters, False otherwise.
    """
    english_alphabet = "abcdefghijklmnopqrstuvwxyz"
    return set(s.lower()).issubset(set(english_alphabet))


def translate_eng_ua(s: str) -> str:
    """
    Translate a given string from English to Ukrainian using a predefined mapping.

    Args:
        s (str): The string to be translated.

    Returns:
        str: The translated string

    """
    table = str.maketrans(LATIN_CHARS, CYRILLIC_CHARS)
    return s.translate(table)


def is_car_plate_chars(s: str) -> bool:
    """
    Check if given string contains only valid characters according to Ukrainian standards
    for car plate. Func() compares chars with LATTIN_CHARS and CYRILLIC_CHARS

    Args:
        s (str): string to be checked.

    Returns:
        bool: True if string consist of allowed chars; False otherwise.
    """
    return set(s).issubset(set(LATIN_CHARS)) or set(s).issubset(set(CYRILLIC_CHARS))


def input_reg_number():
    """
    Get user input for the vehicle registration number and validate its characters.

    Returns:
        str: The validated and translated vehicle number
    """
    reg_number = input("Enter the vehicle registration number: ").upper()
    letters = ''.join(filter(str.isalpha, reg_number))
    if not is_car_plate_chars(letters):
        raise ValueError(f"{reg_number} is not ukrainian vehicle registration number")
    if is_english(letters):
        return translate_eng_ua(reg_number)
    return reg_number


def indetify_region(prefix: str) -> str:
    """
    Identify the region based on the given prefix using data from the 'ua_auto.csv' file.

    Args:
        prefix (str): Two-characters prefix for the vehicle number

    Returns:
        str: The region corresponding to the prefix.
    """
    with open('ua_auto.csv') as f:
        dict_reader = csv.DictReader(f)
        for row in dict_reader:
            if row['Код 2004'] == prefix or row['Код 2013'] == prefix:
                return row['Регіон']
        raise ValueError(f"There is no region with such prefix: \'{prefix}\'")


def main() -> str:
    """
    Main function to execute the script.

    Returns:
        str: The identified region corresponding to the provided vehicle registration number.
    """
    user_input = input_reg_number()
    match = re.search(PATTERN, user_input)
    if match is None:
        raise ValueError(f"{user_input} - is incorrect number")
    code = match.groupdict()
    return indetify_region(code['prefix'])


# -----------client code:------------------
if __name__ == '__main__':

    print(main())
