from json import * #jason enna module aanu ee functions okke ullath(load)
with open("blog.json") as f:
    data=load(f)
print(data)
# aa jason file ne motham angad load cheyyann cheyyunnath.(line by line aayittalla read cheyyunnath)
# encoding error vannal ==> with open("blog.json",encoding='utf-8') as f:

# posts of entered user
user_posts=[post for post in data if post["userId"]==1]
print(user_posts)

# number of likes for postId=3
likes=[len(post["liked_by"]) for post in data if post["postId"]==3][0]
print(likes)

# post liked by userid 2
post=[post for post in data if 2 in post["liked_by"]]
print(post)

# to find max likes
max_likes=(max(data,key=lambda post:len(post["liked_by"]))) #max("ethinte akath ninnanu max kaanunnath",key=lambda)
print(max_likes)