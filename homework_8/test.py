import json
import requests
from datetime import datetime, timedelta
import argparse
from tabulate import tabulate
import csv

CURRENT_DATE = datetime.now().date()
API_URL = "https://api.exchangerate.host/convert"


# Functions---------------------------------------------------------------
def check_entered_currencies(currency_code=str) -> bool:
    """Compare an entered currency code with a list of currency codes."""
    with open('symbols.json') as f:
        data_json = json.loads(f.read())
        keys = data_json['symbols'].keys()
        if currency_code.upper() in keys:
            return True
        else:
            return False


def compare_with_date_now(date, period):
    """Function checks if it is possible to get data in case needs data
    for period of time which have a future Dates.
    date: start_date;
    period: it is a period of time in days."""
    if date + timedelta(days=period) > CURRENT_DATE:
        return False
    return True


def get_currencies_rate(params, period=1):
    outcome = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    date_object = datetime.strptime(params['date'], '%Y-%m-%d').date()
    for p in range(1, period + 1):
        response = requests.get(API_URL, params=params).json()
        rate_values = [response['date'],
                       response['query']['from'],
                       response['query']['to'],
                       response['query']['amount'],
                       response['info']['rate'],
                       response['result']]
        outcome.append(rate_values)
        params['date'] = date_object + timedelta(days=p)
    return outcome


def print_on_screen(data):
    """Print result formatted as table on the terminal outline"""
    print(tabulate(data))


def save_to_csv(data):
    """Save data to csv file"""
    with open("currency_result.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def save_to_txt(data):
    """Save data to txt file"""
    with open("currency_result.txt", "w") as f:
        f.writelines(tabulate(data))


# Parser of command-line-------------------------------------------
parser = argparse.ArgumentParser(
    description='It is a simple and lightweight free service for current '
                'and historical foreign exchange rates & crypto exchange rates.',
    prog='Online currency converter'
)

parser.add_argument('currency_from', type=str, nargs='?', default='USD',
                    help="The three-letter currency code of the currency you would like to convert from. "
                         "default='USD'")
parser.add_argument('currency_to', type=str, nargs='?', default='UAH',
                    help="The three-letter currency code of the currency you would like to convert to. "
                         "default='UAH'")
parser.add_argument('amount', type=float, nargs='?', default=100.00,
                    help='The amount to be converted. default=100.00.')
parser.add_argument('-sd', '--start_date', type=str, nargs='?', default=CURRENT_DATE.strftime('%Y-%m-%d'),
                    help='To get currency rate for specific date, please use '
                         'date in format "YYYY-MM-DD"')
parser.add_argument('-d', '--days', type=int, nargs='?', default=1,
                    help="Period of time for which need to get exchange rates in days "
                         "start from '--start_date'-date. If this period greater than 1 days, it can't be"
                         "applied for request with start_date which is equal to current date")
parser.add_argument('--display', action='store_true', help="Display results on the screen")
parser.add_argument('--save_to_csv', action='store_true', help="Save result in csv format")
parser.add_argument('--save_to_file', action='store_true', help="Save result in txt-file")

args = parser.parse_args()

# Main script-----------------------------------------------
currency_from = args.currency_from
currency_to = args.currency_to
amount = args.amount
start_date = args.start_date
period_days = args.days

if datetime.strptime(start_date, '%Y-%m-%d').date() > CURRENT_DATE:
    start_date = CURRENT_DATE.strftime('%Y-%m-%d')

params = {'date': start_date,
          'from': currency_from,
          'to': currency_to,
          'places': 2,
          'amount': amount}

# Checking the correctness of entered currency codes, if one is wrong, script -
# will not be executed :
if check_entered_currencies(args.currency_from) is False:
    print(f"Incorrect currency code: {args.currency_from}")
if check_entered_currencies(args.currency_to) is False:
    print(f"Incorrect currency code: {args.currency_to}")
if compare_with_date_now(datetime.strptime(start_date, '%Y-%m-%d').date(), period_days - 1) is False:
    print(f"{period_days} days - it's too big period times, which include Future Date. "
          f"Try lesser period.")
else:
    exchange_rates_result = get_currencies_rate(params, period_days)
    if args.display is True:
        print_on_screen(exchange_rates_result)
    if args.save_to_csv is True:
        save_to_csv(exchange_rates_result)
    if args.save_to_file is True:
        save_to_txt(exchange_rates_result)


