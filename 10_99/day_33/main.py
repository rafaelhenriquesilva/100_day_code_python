# API - Application Programming Interface
# Request -> Call a external response
# Response -> Result of resquests

# Restaurant | Kitchen 
# MENU / If finish the ingredients -> Finalize that plate -> API is the MENU

# Example of APIS
"""
- https://docs.cdp.coinbase.com/coinbase-app/docs/welcome
http://api.open-notify.org/iss-now.json

HTTP STATUS
1XX: HOLD ON
2XX: HERE YOU GO
3XX: GO AWAY
4XX: YOU SCREWED UP
5XX: I SCREWED UP
"""

import requests 

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
iss_position = data['iss_position']
longitude = iss_position['longitude']
latitude = iss_position['latitude']
print(longitude)
print(latitude)

