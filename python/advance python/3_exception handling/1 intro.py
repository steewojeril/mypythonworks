# exception handling- handling exception errors
# exception errors - input kodukkumbol aa input ne depend cheyyunna errors
#                 - errors arrising depending on inputs, not because of program


# num1=int(input("enter num1"))  1
# num2=int(input("enter num2"))  0
#print(num1/num2)   1/0




# 3 blocks

# try : exception varaan chance ulla "code" ithil add cheyyuka
# except : athinte solution ivide add cheyyuka
# finally


num1=int(input("enter num1"))
num2=int(input("enter num2"))

try:
    print(num1/num2) #ith mathram koduthatt karyam illa . ahould give solution also else error kaanikkum
except: #error vann kazhinjal
    print("zero division error")
finally:
    print("inside") # like pass


