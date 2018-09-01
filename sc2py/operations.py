import json
import requests


class Operations:

    def operations_structure(self, structure):
        return json.dumps({"operations": structure,}).encode(encoding='utf-8')


class Vote(Operations):
    def __init__(self, voter, author, permlink, weight=100):
        self.voter = voter
        self.author = author
        self.permlink = permlink
        self.weight = weight

    @property
    def operation(self):
        return self.operations_structure(
            [
                [
                    "vote",
                    {
                        "voter": "{}".format(self.voter),
                        "author": "{}".format(self.author),
                        "permlink": "{}".format(self.permlink),
                        "weight": self.weight * 100
                        }
                    ]
                ]
            )


class CustomJson(Operations):
    def __init__(self, required_posting_auths,
                 custom_json_id, structure,
                 required_auths=[]):
        self.required_posting_auths = required_posting_auths
        self.custom_json_id = custom_json_id
        self.structure = structure
        self.required_auths = required_auths


    @property
    def operation(self):
        return self.operations_structure(
            [
                [
                    "custom_json",
                    {
                        "required_auths": self.required_auths,
                        "required_posting_auths":["{}".format(self.required_posting_auths)],
                        "id":"{}".format(self.custom_json_id),
                        "json":json.dumps(self.structure)
                        }
                    ]
                ]
            )


class Unfollow(CustomJson):
    def __init__(self, follower, following, what=[]):
        custom_operation_structure = [
            "follow",
            {
                "follower": "{}".format(follower),
                "following": "{}".format(following),
                "what": ["{}".format(what)]
             }]
        super().__init__(
            required_posting_auths=follower,
            custom_json_id="follow",
            structure=custom_operation_structure)


class Follow(Unfollow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.what = "blog"


class Mute(Unfollow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.what = "ignore"


class Reblog(CustomJson):

    def __init__(self, account, author, permlink):
        custom_operation_json = [
            "reblog",
                {
                    "account": "{}".format(account),
                    "author": "{}".format(author),
                    "permlink": "{}".format(permlink)
                }]
        super().__init__(
            required_posting_auths=account,
            custom_json_id="follow",
            structure=custom_operation_json)


class DeleteComment(Operations):

    def __init__(self, author, permlink):
        self.author = author
        self.permlink = permlink

    @property
    def operation(self):
        return self.operations_structure(
            [
                [
                    "delete_comment", {
                        "author": self.author,
                        "permlink": self.permlink}
                    ]
                ]
            )


class ClaimRewardBalance(Operations):

    def __init__(self, account, reward_steem,
                 reward_sbd, reward_vests):
        self.account = account
        self.reward_steem = reward_steem
        self.reward_vests = reward_vests
        self.reward_sbd = reward_sbd

    @property
    def operation(self):
        return self.operations_structure(
            [
                [
                    "claim_reward_balance", {
                        "account": self.account,
                        "reward_steem": self.reward_steem,
                        "reward_sbd": self.reward_sbd,
                        "reward_vests": self.reward_vests,}
                    ]
                ]
            )


class Comment(Operations):

    def __init__(self, parent_permlink, author,
                permlink, title, body, json_metadata):
        self.parent_permlink = parent_permlink
        self.author = author
        self.permlink = permlink
        self.title = title
        self.body = body
        self.json_metadata = json_metadata

    @property
    def operation(self):
        return self.operations_structure([self.get_json_data])

    @property
    def get_json_data(self):
        return [
            "comment",{
                "parent_author": "",
                "parent_permlink": "{}".format(self.parent_permlink),
                "author": "{}".format(self.author),
                "permlink": "{}".format(self.permlink),
                "title": "{}".format(self.title),
                "body": "{}".format(self.body),
                "json_metadata": json.dumps(self.json_metadata)}
            ]


class CommentOptions(Operations):

    def __init__(self, comment_class=None, beneficiaries=None, max_accepted_payout=100000.000,
                 percent_steem_dollars=10000, allow_votes=True, allow_curation_rewards=True):
        self.comment_class = comment_class
        self.author = comment_class.author
        self.permlink = comment_class.permlink
        self.beneficiaries = beneficiaries or ""
        self.max_accepted_payout = max_accepted_payout
        self.percent_steem_dollars = percent_steem_dollars
        self.allow_votes = allow_votes
        self.allow_curation_rewards = allow_curation_rewards

    @property
    def operation(self):
        return self.operations_structure(
            [self.comment_class.get_json_data, [
                "comment_options",
                {
                    "author": "{}".format(self.author),
                    "permlink": "{}".format(self.permlink),
                    "max_accepted_payout": "100000.000 SBD",
                    "percent_steem_dollars": 10000,
                    "allow_votes": True,
                    "allow_curation_rewards": True,
                    "extensions": [[0, {"beneficiaries": self.beneficiaries}]]
                    }
                ]
             ]
            )
