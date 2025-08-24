import requests
import os
from twilio.rest import Client

api_key=os.environ.get('API_KEY')

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')

parameters={
    'lat':os.environ.get('LAT'),
    'lon':os.environ.get('LON'),
    'appid':api_key,
    'cnt':4
}
responce=requests.get(url='https://api.openweathermap.org/data/2.5/forecast',params=parameters)
responce.raise_for_status()
data=responce.json()
is_raining=False
for i in data['list']:
    if(i['weather'][0]['id']<700):
        is_raining=True
        break
if(is_raining):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain. Don't forget the Umbrella ☂️",
        from_=os.environ.get('TWILLIO_NO'),
        to=os.environ.get('WHATSAPP_NO')
    )
    print(message.status)