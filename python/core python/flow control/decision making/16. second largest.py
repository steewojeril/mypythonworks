# find second largest number
num1=int(input("enter number 1"))  #100   80    60   (check all these condition)
num2=int(input("enter number 2")) #60     100    80
num3=int(input("enter number 3")) #80       60    100

#if we need to find "second largest" we need to find which is the "largest"

if(num1>num2)&(num1>num3):#100>60 &100>80
    # now reming is num2 &num3
    if(num2>num3):    #nested if(writing if block in another if block)
        print("second largest is",num2)
    else:
        print("second largest is",num3)
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print("second largest is",num1)
    else:
        print("second largest is",num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("second largest is",num1)
    else:
        print("second largest is",num2)
else:
    print("invalid") #programme will work if this "else" is not entered