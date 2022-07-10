# check given num is + or -
num=(int(input("enter the number")))  #-2
if(num>0):  #<0 so this block won't work, will enter the next block(else)
    print("the number is positive")
else:
    print("the number is negative")