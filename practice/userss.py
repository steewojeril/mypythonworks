
# user with most followers
# print followingg allathavarude suggestions (eg:id 2 userkk ulla suggestion)
import random
from json import *
with open("users.json") as f:
    data=load(f)
print(data)
fol=[len(user["followers"]) for user in data if user["id"]==2]
print(fol)
print(max(data,key=lambda user:len(user["followers"])))


my_fol=[user["following"] for user in data if user["id"]==1]
my_fol=my_fol.pop() # pop cheythal lastthe element kittum(last aayum firt aayum orenname ullu) [0] kk pakaram use cheyyunnath
print(my_fol)
user=[user for user in data if user["id"] not in my_fol]
random.shuffle(user)
print(user[:2])