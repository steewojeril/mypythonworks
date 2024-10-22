# programme to display "hello" if entered number is multiple of 5 else print "bye"
num=int(input("enter number"))
rem=num%5
if(rem==0):
    print("hello")
else:
    print("bye")


# to print largest number among two numbers
num1=int(input("enter number 1"))
num2=int(input("enter number 2"))
if(num1>num2):
    print("largest number is",num1)
else:
    print("largest number is",num2)