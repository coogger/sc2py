from operations import Operations
from operations import Vote
from operations import Unfollow
from operations import Follow
from operations import Reblog
from operations import Comment
from operations import Comment_options
from sc2py import Sc2

vote = Vote("voter", "author", "permlink", 100)
print(vote.json)

unfollow = Unfollow("follower","following")
print(unfollow.json)

follow = Follow("follower","following")
print(follow.json)

reblog = Reblog("account", "author", "permlink")
print(reblog.json)

comment = Comment("parent_permlink","author","permlink","title","body","son_metadata")
print(comment.json)

beneficiaries = {"account":"coogger","weight":1000},{"account":"hakancelik","weight":100}
comment_options = Comment_options("uthor","permlink",beneficiaries)
print(comment_options.json)

beneficiaries = {"account":"coogger","weight":1000},{"account":"hakancelik","weight":100}
comment_options = Comment_options("author","permlink",beneficiaries)
comment = Comment("parent_permlink","author","permlink","title","body","son_metadata")
json = comment.json+comment_options.json
op = Operations(json).json
sc2 = Sc2(token = "token",data = op)
print(sc2.run)
