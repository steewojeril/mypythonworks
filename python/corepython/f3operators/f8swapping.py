# using third variable
num1=10
num2=20
print("before swapping")
print("num1=",num1)
print("num2=",num2)
temp=num1 #temp=10
num1=num2 #num1=20
num2=temp #num2=10
print("after swapping")
print("num1=",num1)
print("num2=",num2)

# .......................................

# using arithmetic swapping
num1=10
num2=20
print("before swapping")
print("num1=",num1)
print("num2=",num2)
num1=num1+num2 #num1=30
num2=num1-num2  #num2=30-20=10
num1=num1-num2  #num1=30-10=20
print("after swapping")
print("num1=",num1)
print("num2=",num2)


# ................................................

# # another mtd of variable declaration(in single line)
# num1,name,age,location=10,'steewo',23,'thrissur'

# single line swapping
num1,num2=10,20
num1,num2=num2,num1
print(num1)
print(num2)






