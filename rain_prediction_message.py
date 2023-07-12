import datetime
from twilio.rest import Client
import requests
account_sid = "AC602e5f1e63f5c7b7f26cf1c4de6475a1"
auth_token = "8d9da16a40a17028d8c7a162c9f3af05"
API_KEY="e722ca56f5d45806a4b72891544817af"
phone_number="+14787724404"
lat=25.178577
lon=88.246117
parameters={
    "lat":lat,
    "lon":lon,
    "appid":API_KEY,
    "exclude":"current,minutely,daily"

}
r=False
now=datetime.datetime.now().hour
weather=requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
for i in range(now,now+12):
    condition=weather.json()["hourly"][i]["weather"][0]["id"]
    if condition<700:
        r=True
if r:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="You need an umbrella today.",
        from_=phone_number,
        to='+919749595387'
    )