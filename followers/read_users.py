import random
from json import *
with open("users.json") as f:
    data=load(f)
# no of followers of id 2
follow=[len(user["followers"]) for user in data if user["id"]==2][0]
print(follow)
# user with most followers
print(max(data,key=lambda user:len(user["followers"])))




# for id in all_user:
#     if id not in my_followers:
#         suggestion=[user for user in data if user["id"]==id]
#         print(suggestion)

# tip  : split the question
# print following allathavarude suggestions (eg:id 2 userkk ulla suggestion il athint following ulla aalkal paadilla)

my_fol=[user["following"] for user in data if user["id"]==2]
my_fol=my_fol.pop() # pop cheythal lastthe element kittum(last aayum firt aayum orenname ullu) [0] kk pakaram use cheyyunnath
print(my_fol)
user=[user for user in data if user["id"] not in my_fol]
print(user)

#or (sir)
all_user=[user["id"] for user in data ]
print(all_user)
my_fol=[user["following"] for user in data if user["id"]==2][0]
print(my_fol)
print(set(all_user) - set(my_fol))

#
# def get_user():
#     random.shuffle(all_user)
#     return all_user[:3] #[0:3]
# print(get_user())
#
