import requests
# To use variables enviroment
import os
# Auth to test = https://home.openweathermap.org/api_keys
# Verify weather on world: https://www.ventusky.com/
# latitude and longitude: https://www.latlong.net/convert-address-to-lat-long.html
# Cloud Python = https://www.pythonanywhere.com/

url = f'https://api.openweathermap.org/data/2.5/weather'

def check_weather(latitude, longitude):
    parameters = {
        'lat': latitude,
        'lon': longitude,
        'appid': os.environ.get('API_KEY'),
        "cnt": 4
    }

    response = requests.get(url, params=parameters)
    response.raise_for_status()

    data = response.json()
    return data

weather = check_weather( 42.256180, -8.683230)
print(weather)