# sc2py
SteemConnect2 with pyhton

## Getting Started
For general information about SteemConnect V2 and setting up your app please see 
this post from @noisy: 
- [How to configure SteemConnect v2 and use it with your application](https://busy.org/steemconnect/@noisy/how-to-configure-steemconnect-v2-and-use-it-with-your-application-how-it-works-and-how-it-is-different-from-v1)
and this post 
- [ann-introducing-python-social-auth-steemconnect-library-integrate-steemconnect-v2-in-your-python-app-in-5-minutes-design-pack-as](https://steemit.com/steemconnect/@noisy/ann-introducing-python-social-auth-steemconnect-library-integrate-steemconnect-v2-in-your-python-app-in-5-minutes-design-pack-as)

## Firstly
```python
from sc2py import Sc2
sc = Sc2(access_token = "user access key")
```

### Vote
The vote() method will cast a vote on the specified post or comment from the current user:
```python
sc.vote(voter, author, permlink, weight)
```
Parameters:
- voter: The Steem username of the current user.
- author: The Steem username of the author of the post or comment.
- permlink: The link to the post or comment on which to vote. This is the portion of the URL after the last "/". For example the "permlink" for this post: https://steemit.com/steem/@ned/announcing-smart-media-tokens-smts would be "announcing-smart-media-tokens-smts".
- weight: The weight of the vote. 10000 equale a 100% vote.


### post
The post() method will share a post from the current user:
```python
sc.post(parent_permlink,author,permlink,title,body,app,tags)
```

Parameters:
- parent_permlink: The Steem username of the current user.
- app : busy, dlive so this parameter is your app name.
- tags : post's tags of the current user. ex : ["coogger","tr","steem"] etc.



### resteem
```python
sc.resteem(account, author, permlink)
```

### follow
```python
sc.follow(follower,following)
```
