# sc2py
SteemConnect2 with pyhton

## Getting Started
For general information about SteemConnect V2 and setting up your app please see
this post from @noisy:
- [How to configure SteemConnect v2 and use it with your application](https://busy.org/steemconnect/@noisy/how-to-configure-steemconnect-v2-and-use-it-with-your-application-how-it-works-and-how-it-is-different-from-v1)
and this post
- [ann-introducing-python-social-auth-steemconnect-library-integrate-steemconnect-v2-in-your-python-app-in-5-minutes-design-pack-as](https://steemit.com/steemconnect/@noisy/ann-introducing-python-social-auth-steemconnect-library-integrate-steemconnect-v2-in-your-python-app-in-5-minutes-design-pack-as)

- [Django application - django_steemconnect](https://github.com/hakancelik96/django_steemconnect)

### Installation
`pip install sc2py`

### update
`pip install sc2py - U`

## How to use it ?

#### First let's include the library in our project

```python
from sc2py.client import Client
from sc2py.steemconnect import SteemConnect
from sc2py.operations import Vote
from sc2py.operations import CustomJson
from sc2py.operations import Unfollow
from sc2py.operations import Follow
from sc2py.operations import Mute
from sc2py.operations import Reblog
from sc2py.operations import DeleteComment
from sc2py.operations import ClaimRewardBalance
from sc2py.operations import Comment
from sc2py.operations import CommentOptions

c = Client(client_id:str, redirect_url:str, code=False, scope=None)
# scope is None : default scopes = "login,offline,vote,comment,delete_comment,comment_options,custom_json,claim_reward_balance"
# if code is True,you can get refresh_token using ,get_refresh_token()
c.get_authorize_url()
c.get_refresh_token(code:str, app_secret:str)
c.me(access_token:str)
```
- [scopes](https://github.com/steemit/steemconnect/wiki/OAuth-2#scopes)
- [wiki/OAuth-2#code-authorization-flow](https://github.com/steemit/steemconnect/wiki/OAuth-2#code-authorization-flow)


### Vote

The Vote() method will cast a vote on the specified post or comment from the current user:

```python
vote = Vote(voter:str, author:str, permlink:str, weight:int)
response = SteemConnect(token="your_access_token", data=vote.operation).run
if response.status_code == 200:
    print("Your post upvoted")
```
Parameters:
- voter: The Steem username of the current user.
- author: The Steem username of the author of the post or comment.
- permlink: The link to the post or comment on which to vote. This is the portion of the URL after the last "/". For example the "permlink" for this post: https://steemit.com/steem/@ned/announcing-smart-media-tokens-smts would be "announcing-smart-media-tokens-smts".
- weight: The weight of the vote. 100 equale a 100% vote.

### CustomJson

```python
custom_json = CustomJson(required_posting_auths:str, custom_json_id:str, structure:json, required_auths:list)
response = SteemConnect(token="your_access_token", data=custom_json.operation).run
if response.status_code != 200:
    print("Your operation is success")
```

### Follow

```python
follow = Follow(follower:str,following:str)
response = SteemConnect(token="your_access_token", data=follow.operation).run
if response.status_code != 200:
    print("Your operation is success")
```

### Unfollow

```python
unfollow = Unfollow(follower:str,following:str)
response = SteemConnect(token="your_access_token", data=unfollow.operation).run
if response.status_code != 200:
    print("Your operation is success")
```

### Mute

```python
mute = Mute(follower:str,following:str)
response = SteemConnect(token="your_access_token", data=mute.operation).run
if response.status_code != 200:
    print("Your operation is success")
```

### Reblog

```python
reblog = Reblog(account:str, author:str, permlink:str)
response = SteemConnect(token="your_access_token", data=reblog.operation).run
if response.status_code != 200:
    print("Your operation is success")
```


### Comment

```python
comment = Comment(parent_permlink:str,author:str,permlink:str,title:str,body:str,json_metadata:dict)
response = SteemConnect(token="your_access_token", data=comment.operation).run
if response.status_code != 200:
    print("Your operation is success")
```

### Comment with Comment_options

```python
comment_class = Comment(parent_permlink:str, author:str, permlink:str, title:str, body:str, json_metadata:dict)
comment_options = CommentOptions(
    comment_class = comment_class
    beneficiaries,
    max_accepted_payout:int, # default 100000.000
    percent_steem_dollars:int, # default 10000
    allow_votes:bool, # default True
    allow_curation_rewards:bool #default True
)

"""beneficiaries ex :
[
  {"account":"coogger.wallet","weight":500},
  {"account":"coogger.pay","weight":500},
  {"account":"hakancelik","weight":500}
]"""

response = SteemConnect(token="your_access_token", data=comment_options.operation).run
if response.status_code != 200:
    print("Your operation is success")
```

### DeleteComment

```python
delete_comment = DeleteComment(author:str, permlink:str)
response = SteemConnect(token="your_access_token", data=delete_comment.operation).run
if response.status_code != 200:
    print("Your operation is success")
```

### ClaimRewardBalance

```python
claim_reward_balance = ClaimRewardBalance(account:str, reward_steem:str, reward_sbd:str, reward_vests:str)
response = SteemConnect(token="your_access_token", data=claim_reward_balance.operation).run
if response.status_code != 200:
    print("Your operation is success")
```
