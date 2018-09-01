from steemconnect.operations import *
from steemconnect.steemconnect import SteemConnect

class Token:
    def __init__(self):
        token = "xxxxxxxxxxxx"
        self.sc2_run = SteemConnect(token=token, data=self.test_class.operation).run.text
        print(self.sc2_run)


class VoteTest(Token):
    def __init__(self, voter, author, permlink, weight):
        self.test_class = Vote(voter, author, permlink, weight)
        super().__init__()


class CustomJsonTest(Token):
    def __init__(self, required_posting_auths, custom_json_id, structure):
        self.test_class = CustomJson(required_posting_auths, custom_json_id, structure)
        super().__init__()


class UnfollowTest(Token):
    def __init__(self, follower, following):
        self.test_class = Unfollow(follower, following)
        super().__init__()


class FollowTest(Token):
    def __init__(self, follower, following):
        self.test_class = Follow(follower, following)
        super().__init__()


class MuteTest(Token):
    def __init__(self, follower, following):
        self.test_class = Mute(follower, following)
        super().__init__()


class ReblogTest(Token):
    def __init__(self, account, author, permlink):
        self.test_class = Reblog(account, author, permlink)
        super().__init__()


class DeleteCommentTest(Token):
    def __init__(self, author, permlink):
        self.test_class = DeleteComment(author, permlink)
        super().__init__()


class ClaimRewardBalanceTest(Token):
    def __init__(self, account, reward_steem, reward_sbd, reward_vests):
        self.test_class = ClaimRewardBalance(account, reward_steem, reward_sbd, reward_vests)
        super().__init__()


class CommentTest(Token):
    def __init__(self, parent_permlink, author, permlink, title, body, json_metadata):
        self.test_class = Comment(parent_permlink, author, permlink, title, body, json_metadata)
        super().__init__()


class CommentOptionsTest(Token):
    def __init__(self, comment_class=None, beneficiaries=None, max_accepted_payout=100000.000,
                 percent_steem_dollars=10000, allow_votes=True, allow_curation_rewards=True):
        self.test_class = CommentOptions(comment_class, beneficiaries, max_accepted_payout,
                     percent_steem_dollars, allow_votes, allow_curation_rewards)
        super().__init__()



# VoteTest(voter="postdestek", author="chbartist", permlink="a-step-back-or-two", weight=1)
#
# structure = [
#     "test",
#     {
#         "tester": "postdestek",
#         "test_class": "CustomJson class",
#         "what": ["test"]
#      }]
# CustomJsonTest(required_posting_auths="postdestek", custom_json_id="test", structure=structure)
#
# UnfollowTest("postdestek", "hakancelik")
#
# FollowTest("postdestek", "hakancelik")
#
#  MuteTest("postdestek", "hakancelik")
#
# ReblogTest(account="postdestek", author="hakancelik", permlink="coogger-api-update-coogger-python-v021-how-to-use-coogger-python")
#
# DeleteCommentTest(author="postdestek", permlink="test-jsadas12")

# ClaimRewardBalanceTest(account="postdestek", reward_steem, reward_sbd, reward_vests)
# json_metadata = {
#     "format": "markdown",
#     "tags": "test",
#     }
# CommentTest(parent_permlink="test", author="postdestek", permlink="1213-sada1test", title="title", body="body", json_metadata=json_metadata)

# json_metadata = {
#     "format": "markdown",
#     "tags": "test",
#     }
# comment_class = Comment(
#     parent_permlink="test", author="postdestek",
#     permlink="121qweqw3-sada1test", title="title",
#     body="body", json_metadata=json_metadata
# )
#
# beneficiaries = [{"account": "hakancelik", "weight": 1000}]
# CommentOptionsTest(comment_class=comment_class, beneficiaries=beneficiaries)
