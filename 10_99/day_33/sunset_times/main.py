import requests

iss_response = requests.get("http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

iss_data = iss_response.json()
iss_position = iss_data['iss_position']
longitude = iss_position['longitude']
latitude = iss_position['latitude']

parameters = {
    'lat': latitude,
    'lng': longitude
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()['results']
print(data)