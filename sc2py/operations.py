import json


class Vote:
    def __init__(self, voter, author, permlink, weight=100):
        self.voter = voter
        self.author = author
        self.permlink = permlink
        self.weight = weight

    @property
    def json(self):
        return [
            "vote",
                {
                    "voter": "{}".format(self.voter),
                    "author": "{}".format(self.author),
                    "permlink": "{}".format(self.permlink),
                    "weight": self.weight * 100
                }],


class Unfollow:
    def __init__(self, follower, following, what=[]):
        self.follower = follower
        self.following = following
        self.what = what

    @property
    def json(self):
        follow_json = [
            "follow",
                {
                    "follower": "{}".format(self.follower),
                    "following": "{}".format(self.following),
                    "what": ["{}".format(self.what)]
                }]
        return [
            "custom_json",
                {
                    "required_auths": [],
                    "required_posting_auths":["{}".format(self.follower)],
                    "id":"follow",
                    "json":json.dumps(follow_json)
                }],


class Follow(Unfollow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.what = "blog"


class Mute(Unfollow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.what = "ignore"


class Reblog:

    def __init__(self, account, author, permlink):
        self.account = account
        self.author = author
        self.permlink = permlink

    @property
    def json(self):
        reblog_json = [
            "reblog",
                {
                    "account": "{}".format(self.account),
                    "author": "{}".format(self.author),
                    "permlink": "{}".format(self.permlink)
                }]
        return [
            "custom_json",
            {
                "required_auths": [],
                "required_posting_auths":["{}".format(self.account)],
                "id":"follow",
                "json":json.dumps(reblog_json)
            }],


class Comment:

    def __init__(self, parent_permlink, author,
                permlink, title, body, json_metadata):
        self.parent_permlink = parent_permlink
        self.author = author
        self.permlink = permlink
        self.title = title
        self.body = body
        self.json_metadata = json_metadata

    @property
    def json(self):
        return ["comment",
                {
                    "parent_author": "",
                    "parent_permlink": "{}".format(self.parent_permlink),
                    "author": "{}".format(self.author),
                    "permlink": "{}".format(self.permlink),
                    "title": "{}".format(self.title),
                    "body": "{}".format(self.body),
                    "json_metadata": json.dumps(self.json_metadata)
                }],

    def comment_options(self, beneficiaries,
        max_accepted_payout=100000.000,
        percent_steem_dollars=10000,
        allow_votes=True,
        allow_curation_rewards=True):
        return ["comment",
            {
                "parent_author": "",
                "parent_permlink": "{}".format(self.parent_permlink),
                "author": "{}".format(self.author),
                "permlink": "{}".format(self.permlink),
                "title": "{}".format(self.title),
                "body": "{}".format(self.body),
                "json_metadata": json.dumps(self.json_metadata)
                }], ["comment_options",
                {
                    "author": "{}".format(self.author),
                    "permlink": "{}".format(self.permlink),
                    "max_accepted_payout": "100000.000 SBD",
                    "percent_steem_dollars": 10000,
                    "allow_votes": True,
                    "allow_curation_rewards": True,
                    "extensions": [[0, {"beneficiaries": beneficiaries}]]
                }]


class DeleteComment:

    def __init__(self, author, permlink):
        self.author = author
        self.permlink = permlink

    @property
    def json(self):
        return [
            "delete_comment", {
                "author": self.author,
                "permlink": self.permlink
            }
        ],


class ClaimRewardBalance:

    def __init__(self, account, reward_steem, reward_sbd, reward_vests):
        self.account = account
        self.reward_steem = reward_steem
        self.reward_vests = reward_vests
        self.reward_sbd = reward_sbd

    @property
    def json(self):
        return [
            "claim_reward_balance", {
                "account": self.account,
                "reward_steem": self.reward_steem,
                "reward_sbd": self.reward_sbd,
                "reward_vests": self.reward_vests,
            }
        ],


class Operations:

    def __init__(self, json):
        self.payload = {"operations": json}

    @property
    def json(self):
        return json.dumps(self.payload).encode(encoding='utf-8')
