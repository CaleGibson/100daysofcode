import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

API_KEY = ""
Endpoint = "https://api.openweathermap.org/data/2.5/weather"
account_sid = ""
auth_token = "
client = Client(account_sid, auth_token)

paramaters = {
    "lat": 
    "lon": 
    "appid": API_KEY,
}

response = requests.get(Endpoint, params=paramaters)
response.raise_for_status()
data = response.json()
#if the API link still worked we couldve sliced through to find 12 hours into the future to check all day weather
comp = data["weather"][0]["id"]

is_rain = True
if comp < 800:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    is_rain = True
if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_=
        to=
    )

    print(message.status)
