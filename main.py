#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import requests
import os
from twilio.rest import Client

# OpenWeather Api Key
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
# Environmental variable for api_key
api_key = os.environ.get("OWM_API_KEY")

# Environmental variables for account_sic, auth_token
# Identification for Twilio account
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

# Latitude and longitude of Toronto
MY_LAT = 43.640980 # Your latitude
MY_LONG = -79.400461 # Your longitude

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
# Get id if it is going to rain for the next 12 hours
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True

# If id > 700, it will rain, send text message via twilio
if will_rain:
    client = Client (account_sid, auth_token)
    message = client.messages \
        .create (
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+1**********", // Twilio Phone number
        to="+1**********"   // Phone number used to create Twilio Account
    )

    print(message.status)
