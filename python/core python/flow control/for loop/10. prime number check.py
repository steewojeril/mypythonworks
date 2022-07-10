# print prime numbers
#  2, 3,5, 7, 11, 13
# a number is said to be prime number it is factor of 1 and that number only
# 7 is a prime number means it is factor of 1 and 7 only ( not a factor of 2 to 6 )

num=int(input("enter the number"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1
        break

if(flag>0):
    print(num, "is not prime")
else:
    print(num,"is prime")

