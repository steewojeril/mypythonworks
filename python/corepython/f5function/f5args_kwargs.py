# *arg - positional arguments- data type: tuple
# def printvalue(num1,num2):
#     print(num1,num2)
# printvalue(1,2) #if we enter more than 3 it will not work

def printvalue(*args): # we can enter any name after *
    print(args) 
    print(type(args))
    print(args[0])
    print(args[1])
    print(args[2])
printvalue(1,2,"steewo")


# ithil 1, 2, steewo  enthaanennu convey cheyyunnilla(name: steewo, roll:100) thats why we use  **kwargcs- datatype: dic

def print_details(**kwargs):
    print(kwargs)
    print(type(kwargs))
print_details(name="steewo",age=20,place="thrissur") 
