import requests
import json

class Sc2:

    def __init__(self,access_token):
        self.access_token = access_token
        self.sc2_broadcast = "https://v2.steemconnect.com/api/broadcast"

    def vote(self, voter, author, permlink, weight = 10000):
        payload = {
        "operations":
            [
                ["vote",
                    {
                        "voter":"{}".format(voter),
                        "author":"{}".format(author),
                        "permlink":"{}".format(permlink),
                        "weight":weight * 100
                    }
                ]
            ]
        }
        return self.run(payload)

    def follow(self,follower,following):
        payload = {
            "operations":
                [
                    ["custom_json",
                        {
                            "required_auths":[],
                            "required_posting_auths":["{}".format(follower)],
                            "id":"follow",
                            "json":"[\"follow\",{\"follower\":\"%s\""%follower+",\"following\":\"%s\""%following+",\"what\":[]}]"
                        }
                    ]
                ]
        }
        return self.run(payload)

    def resteem(self, account, author, permlink):
        payload = {
            "operations":
                [
                    ["custom_json",
                        {
                             "required_auths":[],
                             "required_posting_auths":["{}".format(account)],
                             "id":"follow",
                             "json":"[\"reblog\",{\"account\":\"%s\""%account+",\"author\":\"%s\""%author+",\"permlink\":\"%s\""%permlink+"}]"
                        }
                    ]
                ]
        }
        return self.run(payload)

    def post(self,parent_permlink,author,permlink,title,body,json_metadata):
        payload = {
            "operations":
                 [
                      ["comment",
                           {
                               "parent_author":"",
                               "parent_permlink":"{}".format(parent_permlink),
                               "author":"{}".format(author),
                               "permlink":"{}".format(permlink),
                               "title":"{}".format(title),
                               "body":"{}".format(body),
                               "json_metadata":json.dumps(json_metadata)
                            }
                      ]
                  ]
        }
        return self.run(payload)

    def run(self, payload):
        payload = json.dumps(payload).encode(encoding='utf-8')
        response = requests.post(self.sc2_broadcast, data = payload, headers = self.get_header())
        return response

    def get_header(self):
        return{
        "content-type": "application/json; charset=utf-8",
        "Accept": "application/json",
        "Authorization": self.access_token,
        "cache-control": "no-cache"
        }
