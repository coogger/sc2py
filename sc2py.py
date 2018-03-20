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
                        "voter":"{}",
                        "author":"{}",
                        "permlink":"{}",
                        "weight":{}
                    }
                ]
            ]
        }""".format(voter,author,permlink,weight)
        response = requests.post(self.sc2_broadcast, data = payload, headers = self.headers())
        return response

    def follow(follower,following):
        payload = """{
            "operations":
                [
                    ["custom_json",
                        {
                            "required_auths":[],
                            "required_posting_auths":["{}"],
                            "id":"follow",
                            "json":"[\\"follow\\",{\\"follower\\":\\"{}\\",\\"following\\":\\"{}\\",\\"what\\":[]}]"
                        }
                    ]
                ]
        }""".format(follower,follower,following)
        response = requests.post(self.sc2_broadcast, data = payload, headers = self.headers())
        return response

    def resteem(self, account, author, permlink):
        payload = """{
            "operations":
                [
                    ["custom_json",
                        {
                             "required_auths":[],
                             "required_posting_auths":["{}"],
                             "id":"follow",
                             "json":"[\\"reblog\\",{\\"account\\":\\"{}\\",\\"author\\":\\"{}\\",\\"permlink\\":\\"{}\\"}]"
                        }
                    ]
                ]
        }""".format(account,account,author,permlink)
        response = requests.post(self.sc2_broadcast, data = payload, headers = self.headers())
        return response

    def post(self,parent_permlink,author,permlink,title,body,app,tags):
        payload = """{
            "operations":
                 [
                      ["comment",
                           {
                               "parent_author":"",
                               "parent_permlink":"{}",
                               "author":"{}",
                               "permlink":"{}",
                               "title":"{}",
                               "body":"{}",
                               "json_metadata":"{\\"app\\":\\"{}\\",\\"tags\\":[\\"{}\\"]}"
                            }
                      ]
                  ]
        }""".format(parent_permlink,author,permlink,title,body,app,tags)
        response = requests.post(self.sc2_broadcast, data = payload, headers = self.headers())
        return response

    def get_header(self):
        return{
        "content-type": "application/json; charset=utf-8",
        "Accept": "application/json",
        "Authorization": self.access_token,
        "cache-control": "no-cache"
        }
