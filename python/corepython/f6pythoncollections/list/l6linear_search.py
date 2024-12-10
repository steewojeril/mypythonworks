# linear search

lst=[1,5,7,8,3,6,2,9,15,20]
# to find the entered number is present or not

num=int(input("enter the number"))
flag=0
for i in lst:
    if(i==num):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")

# this method is called 'linear search'
# linear search - for small list
# disadvantage - time consuming
# to overcome this disadvantage we use 'binary search'






# or
num=int(input("enter the number"))
for i in lst:
    if num in lst:
        flag = 1
        break
if (flag > 0):
    print("element found")
else:
    print("element not found")






