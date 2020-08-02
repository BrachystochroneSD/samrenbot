import requests
from credentials import *

url = 'https://api.twitch.tv/helix/webhooks/hub/'
payload = {"hub.mode":"subscribe",
           "hub.topic":"https://api.twitch.tv/helix/users/follows?first=1&to_id=51393318",
           "hub.callback":"http://www.zenocyne.com:5000/TwitchAlert",
           "hub.lease_seconds":"864000"
}

header = {'Client-ID': clientid, 'Authorization': oauth_token}

req = requests.post(url, headers = header, data = payload)
print(req)
print(req.text)
