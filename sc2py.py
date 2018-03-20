from django.utils.text import slugify
import requests

class Sc2:

    def __init__(self,access_token):
        self.access_token = access_token
        self.sc2_broadcast = "https://v2.steemconnect.com/api/broadcast"

    def vote(self, voter, author, permlink, weight = 10000):
        payload = """{
        "operations":
            [
                ["vote",
                    {
                        "voter":"%s",
                        "author":"%s",
                        "permlink":"%s",
                        "weight":%s
                    }
                ]
            ]
        }"""%(voter,author,permlink,weight)
        return self.run(payload)

    def follow(follower,following):
        payload = """{
            "operations":
                [
                    ["custom_json",
                        {
                            "required_auths":[],
                            "required_posting_auths":["%s"],
                            "id":"follow",
                            "json":"[\\"follow\\",{\\"follower\\":\\"%s\\",\\"following\\":\\"%s\\",\\"what\\":[]}]"
                        }
                    ]
                ]
        }"""%(follower,follower,following)
        return self.run(payload)

    def resteem(self, account, author, permlink):
        payload = """{
            "operations":
                [
                    ["custom_json",
                        {
                             "required_auths":[],
                             "required_posting_auths":["%s"],
                             "id":"follow",
                             "json":"[\\"reblog\\",{\\"account\\":\\"%s\\",\\"author\\":\\"%s\\",\\"permlink\\":\\"%s\\"}]"
                        }
                    ]
                ]
        }"""%(account,account,author,permlink)
        return self.run(payload)

    def post(self,author,title,body,tags):
        permlink = slugify(title.lower())
        payload = """{
            "operations":
                 [
                      ["comment",
                           {
                               "parent_author":"",
                               "parent_permlink":"%s",
                               "author":"%s",
                               "permlink":"%s",
                               "title":"%s",
                               "body":"%s",
                               "json_metadata":"{\\"tags\\":[\\"%s\\"]}"
                            }
                      ]
                  ]
        }"""%(tags[0],author,permlink,title,body,tags[0])
        return self.run(payload)

    def run(self, payload):
        response = requests.post(self.sc2_broadcast, data = payload, headers = self.get_header())
        return response

    def get_header(self):
        return{
        "content-type": "application/json; charset=utf-8",
        "Accept": "application/json",
        "Authorization": self.access_token,
        "cache-control": "no-cache"
        }
