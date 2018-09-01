import requests
import json


class Client:

    def __init__(self, client_id, redirect_url, code=False, scope=None):
        self.client_id = client_id
        self.redirect_url = redirect_url
        self.scope = scope or self.scopes()
        self.code = code

    @staticmethod
    def scopes():
        return "login, offline, vote, comment, delete_comment, comment_options, custom_json, claim_reward_balance"

    def get_authorize_url(self):
        api = "https://steemconnect.com/oauth2/authorize?client_id={}&redirect_uri={}&scope={}".format(
            self.client_id, self.redirect_url, self.scope
            )
        if self.code:
            api = api+"&response_type=code"
        return api

    @staticmethod
    def get_refresh_token(code, app_secret):
        "tokens = get_refresh_token(code:str,app_secret:str)"
        "tokens['access_token']"
        "tokens['username']"
        "tokens['refresh_token']"
        token_api = "https://steemconnect.com/api/oauth2/token?code={}&client_secret={}".format(code, app_secret)
        return requests.post(token_api).json()

    @staticmethod
    def me(access_token):
        api = "https://steemconnect.com/api/me"
        headers = {"Authorization": access_token}
        return requests.post(api, headers=headers).json()
