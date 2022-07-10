num1=int(input("enter num1"))
num2=int(input("enter num2"))

try:
    print(num1/num2)
except Exception as e:
    print("error",e)