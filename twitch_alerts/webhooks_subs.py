import requests

class Follow_Subscriptions:
    def __init__(self, channel_id, client_id, callback_url, oauth_token):
        self.channel_id = channel_id
        self.client_id = client_id
        self.oauth_token = oauth_token
        self.lease_seconds = 864000
        self.callback_url = callback_url
        self.url = 'https://api.twitch.tv/helix/webhooks/hub/'

    def subscribe(self):
        header = {
            'Client-ID': self.client_id,
            'Authorization': self.oauth_token
        }

        payload = {
            "hub.mode" : "subscribe",
            "hub.topic" : "https://api.twitch.tv/helix/users/follows?first=1&to_id=" + self.channel_id,
            "hub.callback" : self.callback_url,
            "hub.lease_seconds": self.lease_seconds
        }

        req = requests.post(self.url, headers = header, data = payload)

        print(req)
        print(req.text)
