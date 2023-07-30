from datetime import datetime, timedelta
import requests
from tabulate import tabulate

API_URL = "https://api.exchangerate.host/convert"
CURRENT_DATE = datetime.now().strftime('%Y-%m-%d')
# print(datetime.now().date())

params = {'date': '2023-07-27',
          'from': 'USD',
          'to': 'UAH',
          'places': 2,
          'amount': 100.00}

date_object1 = datetime.strptime(params['date'], '%Y-%m-%d').date()

print(datetime.now().date())
# print(date_object1 + timedelta(days=5))


def compare_with_date_now(date, delta):
    print('compare_with_date_now: ', delta, date)
    print('result: ', date + timedelta(days=delta), datetime.now().date())
    if date + timedelta(days=delta) > datetime.now().date():
        return False
    return True


def get_currencies_rate(params, period=1):
    outcome = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    date_object = datetime.strptime(params['date'], '%Y-%m-%d').date()
    print(date_object)
    if compare_with_date_now(date_object, period - 1) is True:
        pass
    else:
        raise ValueError(f"It's impossible to get currency rate for period {period} days")
    for p in range(1, period+1):
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


# print(compare_with_date_now(date_object1, 5))
result = get_currencies_rate(params, 5)
print(result)
print(tabulate(result))

