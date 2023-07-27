"""3. Отримати прогноз погоди для Одеси на наступні 5 днів
та записати у файл з ім'ям поточної дати
"""
import datetime
import requests


WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/forecast/daily?"
API_ID = "f9ada9efec6a3934dad5f30068fdcbb8"


def get_data_requests(param):
    """Get a weather data. The function returns the json-encoded content"""
    url = WEATHER_API_URL
    response = requests.get(url, params=param)
    return response.json()


def create_name_for_file(data):
    """Create a name for file from json-encoded data. Returns a string"""
    list_dt = data['list'][0]['dt']  # Get date from weather forecast data
    formatted_date = datetime.datetime.fromtimestamp(list_dt).strftime("%d-%m-%Y")
    city_name = data['city']['name']  # Get name of city
    days = data['cnt']  # Get period of forecast in days
    return f"{formatted_date}-{city_name}-{days}-days-weather-forecast"


def create_file_txt(data):
    """The function create a txt-file and write here: date, day temp and
    night temp"""
    f_name = create_name_for_file(data)  # Call outer function for creating file name
    head = "Date / Day, t / Night, t \n"  # First row for the data
    with open(f"{f_name}.txt", 'w') as f:
        f.writelines(f"{head}")
        data_list = data['list']
        for i in range(len(data_list)):
            dt = data['list'][i]['dt']  # Get Date
            date = datetime.datetime.fromtimestamp(dt).strftime("%d-%m-%Y")  # get formatted Date
            day_temp = data['list'][i]['temp']['day']  # get day temperature
            night_temp = data['list'][i]['temp']['night']  # get night temperature
            f.writelines(f"{date} / {day_temp} / {night_temp} \n")


def user_forecast_request():
    """Gets user's weather forecast request and returns a tuple
     with name of required city and forecast period in days """
    city = input("Enter the name of city for which you need weather forecast: ")
    days = input("For how many days in advance you need forecast?: ")
    return city, int(days)


params = dict(appid=API_ID, units='metric')  # Create dict with params
params['q'], params['cnt'] = user_forecast_request()  # Add user request to params


forecast_data = get_data_requests(params)  # Get weather forecast
create_file_txt(forecast_data)  # Create a file with forecast data
