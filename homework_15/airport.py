"""У вкладенні файл csv з даними про аеропорти світу, написати програму
яка зможе повернути дані за такими параметрами:
--iata_code - код аеропорту, має повернути 1 запис за кодом аеропорту (ввесь рядок)
або повернути помилку AirportNotFoundError

--country - країна, що має повернути всі записи по аеропортах або

CountryNotFoundError

--name - значення імені аеропорту, допустимо входження рядка хоча б мінімально,
тобто liman повинен повернути рядки з такими назвами:

Ilimanaq Heliport
Sidi Slimane Airport
Kilimanjaro International Airport
West Kilimanjaro Airport
Limanske Airfield
Liman Airfield
...
або AirportNotFoundError

Тільки один параметр є обов'язковим, якщо вибрано декілька - повернути помилку:

MultipleOptionsError, якщо жодного - NoOptionsFoundError

** дод. помилки приймають два аргументи, текст помилки та вхідні дані, приклад:

AirportNotFoundError: ('Airport not found', 'OESD')
CountryNotFoundError: ('Country not found', 'UGUGU')
IATA код може бути лише 3х буквеним у верхньому регістрі, зробити валідацію на
нього або повернути IATACodeError"""

import csv
import argparse
import re


# ----------------------class of exception------------------
class AirportNotFoundError(Exception):
    """
    Exception raised when an airport with a specific IATA code is not found.

    Attributes:
        message (str): A message explaining the exception.
        code (str): The IATA code that was not found.
    """
    def __init__(self, message: str, code: str):
        self.message = message
        self.code = code


class CountryNotFoundError(Exception):
    """
    Exception raised when a country with a specific ISO country code is not found.

    Attributes:
        message (str): A message explaining the exception.
        code (str): The ISO country code that was not found.
    """
    def __init__(self, message: str, code: str):
        self.message = message
        self.code = code


class NoOptionsFoundError(Exception):
    """
    Exception raised when no search options are chosen.

    This exception is raised when the user runs the script without specifying any search option.
    """
    pass


class MultipleOptionsError(Exception):
    """
    Exception raised when multiple search options are chosen.

    This exception is raised when the user runs the script with more than one search option.
    """
    pass


class IATACodeError(Exception):
    def __init__(self, message: str, code: str):
        self.message = message
        self.code = code


# ------------------------functions---------------------------
AIRPORT_CODES_CSV = 'airport-codes_csv.csv'


def validate_iata_code(code: str):
    """
   Validate the correctness of an IATA code.

   This function checks if the provided IATA code is a valid 3-character uppercase string.

   Args:
       code (str): The IATA code to validate.

   Returns:
       bool: True if the code is valid.

   Raises:
       IATACodeError: If the provided code is not a valid IATA code.
   """
    if len(code) != 3 or code != code.upper() or not code.isalpha():
        raise IATACodeError("Incorect IATA code", code)
    return True


def get_by_iata_code(code: str):
    """
    Retrieve airport information by IATA code.

    This function retrieves information about an airport using its IATA code from a CSV file.

    Args:
        code (str): The IATA code to search for.

    Raises:
        IATACodeError: If the provided IATA code is not valid.
        AirportNotFoundError: If no airport with the provided IATA code is found.
    """
    validate_iata_code(code)
    flag = False
    with open(AIRPORT_CODES_CSV) as f:
        dict_reader = csv.DictReader(f)
        for row in dict_reader:
            if row['iata_code'] == code:
                print(row)
                flag = True
        if not flag:
            raise AirportNotFoundError("Airport not found", code)


def get_by_country(name: str):
    """
    Search for airports in a specific country by its ISO country code.

    Args:
        name (str): The ISO country code to search for.

    Returns:
        str: returns a string(s) with data filtered by country

    Raises:
        CountryNotFoundError: If no country with the provided ISO country code is found.
    """
    flag = False
    with open(AIRPORT_CODES_CSV) as f:
        dict_reader = csv.DictReader(f)
        for row in dict_reader:
            if row['iso_country'].lower() == name.lower():
                print(row)
                flag = True
        if not flag:
            raise CountryNotFoundError('Country not found', name)


def get_by_name(name: str):
    """
    Search for airports by name, allowing partial or full matches.

    Args:
        name (str): The name to search for.

    Returns:
        returns string(s) if airports with the provided name (partial or full) are found

    Raises:
        AirportNotFoundError: If no airports with the provided name (partial or full) are found.
    """
    flag = False
    pattern = re.compile(r"{}".format(name.lower()))
    with open(AIRPORT_CODES_CSV) as f:
        dict_reader = csv.DictReader(f)
        for row in dict_reader:
            match = pattern.search(row['name'].lower())
            if match:
                print(row['name'])
                flag = True
        if not flag:
            raise AirportNotFoundError("Airport not found, name:", name)


def handle_args(arguments: object):
    """
    Handle command-line arguments and validate their usage.

    Args:
        arguments (object Namespace): The parsed command-line arguments.

    Raises:
        NoOptionsFoundError: If no search option is chosen. Use -h for help.
        MultipleOptionsError: If more than one search option is chosen.
    """
    counter = 0
    for k in vars(arguments):
        if vars(arguments)[k]:
            counter += 1
    if counter == 0:
        raise NoOptionsFoundError("One option needs to be chosen, use -h for help")
    if counter > 1:
        raise MultipleOptionsError("Choose only one option")


# The dictionary with search functions
SEARCH_FUNCS = {
    'iata_code': get_by_iata_code,
    'iso_country': get_by_country,
    'name': get_by_name
}


# -----------------------parser------------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="Airport Code Search",
        description=("This airline and airport code search engine provides an "
                     "official source for codes assigned by IATA.")
    )
    parser.add_argument('--iata_code', dest='iata_code', type=str,
                        help="Returns a record of airport with corresponding IATA code")
    parser.add_argument('--country', dest='iso_country', type=str,
                        help="Returns all airport records by country")
    parser.add_argument('--name', dest='name', type=str,
                        help="Returns all airport records where name have full or partial matching")

    args = parser.parse_args()

# --------------------------client-code:----------------------

if __name__ == '__main__':
    handle_args(args)
    for key in vars(args):
        if vars(args)[key] is not None:
            SEARCH_FUNCS[key](vars(args)[key])
