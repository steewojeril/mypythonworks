'''
ARITHMETIC OPERATORS

adddition  +
substraction  -
multiplication  *
division  /
modulus  %  (to fetch reminder)
exponential operator  **  (power operator)
floor division  // (to discard decimal point)

'''

# arithmetic operator
#read two numbers and print their sum

num1=int(input("enter number 1"))  #default data type of input is string. so use int to read the value as integer.
num2=int(input("enter number 2"))  #other wise it will show 1020 if num1 & num2 are 10 & 20 respectively
sum=num1+num2
multi=num1*num2*num3
print(f"sum is{sum}  multiplication is {multi}")


#type - to know the data type of a variable
print(type(num1))