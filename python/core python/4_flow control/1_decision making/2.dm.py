# checking ag is above or below 18

age=int(input("enter age")) #20
if(age>=18):
    print("you can vote")  #20>18 (true) so this block works
else:
    print("you can't vote") #this doesm't


# check given num is + or -

num=(int(input("enter the number")))  #-2
if(num>0):  #<0 so this block won't work, will enter the next block(else)
    print("the number is positive")
else:
    print("the number is negative")



#check given number is even or odd
num=(int(input("enter the number")))
rem=num%2
if(rem==0):
    print("number is even")
else:
    print("number is odd")