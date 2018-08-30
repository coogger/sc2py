import requests


class Sc2:

    def __init__(self, token, data):
        self.token = token
        self.data = data
        self.broadcast_api = "https://v2.steemconnect.com/api/broadcast"
        self.headers = {
            "content-type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "Authorization": self.token,
            "cache-control": "no-cache"
        }

    @property
    def run(self):
        return requests.post(
            self.broadcast_api,
            data=self.data,
            headers=self.headers
        )
