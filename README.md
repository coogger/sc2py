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
from sc2py.sc2py import Sc2
from sc2py.operations import Vote
from sc2py.operations import CustomJson
from sc2py.operations import Unfollow
from sc2py.operations import Follow
from sc2py.operations import Mute
from sc2py.operations import Reblog
from sc2py.operations import Comment
from sc2py.operations import DeleteComment
from sc2py.operations import ClaimRewardBalance
from sc2py.operations import Operations

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
json_data = Operations(json=vote.json).json
response = Sc2(token="your_access_token", data=json_data).run
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
custom_json = CustomJson(required_posting_auths:str, id_:str json_:json)
json_data = Operations(json=custom_json.json).json
response = Sc2(token="your_access_token", data=json_data).run
if response.status_code != 200:
    print(response.text)
```

### Follow

```python
follow = Follow(follower:str,following:str)
json_data = Operations(json=follow.json).json
response = Sc2(token="your_access_token", data=json_data).run
if response.status_code != 200:
    print(response.text)
```

### Unfollow

```python
unfollow = Unfollow(follower:str,following:str)
json_data = Operations(json=unfollow.json).json
response = Sc2(token="your_access_token", data=json_data).run
if response.status_code != 200:
    print(response.text)
```

### Mute

```python
mute = Mute(follower:str,following:str)
json_data = Operations(json=mute.json).json
response = Sc2(token="your_access_token", data=json_data).run
if response.status_code != 200:
    print(response.text)
```

### Reblog

```python
reblog = Reblog(account:str, author:str, permlink:str)
json_data = Operations(json=reblog.json).json
response = Sc2(token="your_access_token", data=json_data).run
if response.status_code != 200:
    print(response.text)
```


### Comment

```python
comment = Comment(parent_permlink:str,author:str,permlink:str,title:str,body:str,json_metadata:dict)
json_data = Operations(json=comment.json).json
response = Sc2(token="your_access_token", data=json_data).run
if response.status_code != 200:
    print(response.text)
```

### Comment with Comment_options

```python
comment = Comment(parent_permlink:str, author:str, permlink:str, title:str, body:str, json_metadata:dict)
comment_options = comment.comment_options(
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

json_data = Operations(json=comment_options).json
response = Sc2(token="your_access_token", data=json_data).run
if response.status_code != 200:
    print(response.text)
```

### DeleteComment

```python
delete_comment = DeleteComment(author:str, permlink:str)
json_data = Operations(json=delete_comment.json).json
response = Sc2(token="your_access_token", data=json_data).run
if response.status_code != 200:
    print(response.text)
```

### ClaimRewardBalance

```python
claim_reward_balance = ClaimRewardBalance(account:str, reward_steem:str, reward_sbd:str, reward_vests:str)
json_data = Operations(json=claim_reward_balance.json).json
response = Sc2(token="your_access_token", data=json_data).run
if response.status_code != 200:
    print(response.text)
```
