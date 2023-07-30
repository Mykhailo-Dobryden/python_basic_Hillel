import json
import requests
from datetime import datetime, timedelta
import argparse
from tabulate import tabulate
import csv

current_date = datetime.now().strftime('%Y-%m-%d')


# Functions---------------------------------------------------------------
def check_entered_currencies(currency_code):
    with open('symbols.json') as f:
        data_json = json.loads(f.read())
        keys = data_json['symbols'].keys()
        if currency_code in keys:
            return True
        else:
            return False


def compare_with_date_now(date, delta):
    print('compare_with_date_now: ', delta, date)
    print('result: ', date + timedelta(days=delta), datetime.now().date())
    if date + timedelta(days=delta) > datetime.now().date():
        return False
    return True


def get_currencies_rate(params, period=1):
    outcome = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    date_object = datetime.strptime(params['date'], '%Y-%m-%d').date()
    if compare_with_date_now(date_object, period - 1) is True:
        pass
    else:
        raise ValueError(f"It's impossible to get currency rate for period {period} days")
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
    with open("currency_result.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def save_to_txt(data):
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
parser.add_argument('-sd', '--start_date', type=str, nargs='?', default=current_date,
                    help='To get currency rate for specific date, please use '
                         'date in format "YYYY-MM-DD"')
parser.add_argument('-d', '--days', type=int, nargs='?', default=1,
                    help="Period of time for which need to get exchange rates in days "
                         "start from --start_date")
parser.add_argument('--display', action='store_true', help="Display results on the screen")
parser.add_argument('--save_to_csv', action='store_true', help="Save result in csv format")
parser.add_argument('--save_to_file', action='store_true', help="Save result in txt-file")

args = parser.parse_args()

# Main script-----------------------------------------------
API_URL = "https://api.exchangerate.host/convert"

# Checking the correctness of entered currency codes:
if check_entered_currencies(args.currency_from) is False:
    print(f"{args.currency_from} is incorrect")
if check_entered_currencies(args.currency_to) is False:
    print(f"{args.currency_to} is incorrect")

currency_from = args.currency_from
currency_to = args.currency_to
amount = args.amount
start_date = args.start_date
period = args.days

params = {'date': start_date,
          'from': currency_from,
          'to': currency_to,
          'places': 2,
          'amount': amount}

if check_entered_currencies(args.currency_from) is False:
    print(f"Incorrect currency code: {args.currency_from}")
elif check_entered_currencies(args.currency_to) is False:
    print(f"Incorrect currency code: {args.currency_to}")
else:
    try:
        exchange_rates_result = get_currencies_rate(params, period)
        if args.display is True:
            print_on_screen(exchange_rates_result)
        if args.save_to_csv is True:
            save_to_csv(exchange_rates_result)
        if args.save_to_file is True:
            save_to_txt(exchange_rates_result)
    except ValueError as e:
        print(e)


