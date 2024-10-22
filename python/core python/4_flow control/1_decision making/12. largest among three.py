# largest among three numbers
num1=int(input("enter number 1"))#100  80  60 (check all these condition)
num2=int(input("enter number 2"))#80  100  80
num3=int(input("enter number 3"))#60  60  100
if(num1>num2)&(num1>num3):#100>80 &100>60  1&1
    print(num1,"is largest")
elif(num2>num1)&(num2>num3):
    print(num2,"is largest")
else:
    print(num3,"is largest")
