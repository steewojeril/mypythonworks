# *arg
# def printvalue(num1,num2):
#     print(num1,num2)
# printvalue(1,2) #if we enter more than 3 it will not work

def printvalue(*arg): # we can enter any name after *
    print(arg) # here we can read multiple numbers (in tuple) //  if we print(*arg) print innormal way
printvalue(1,2)


def print_details(*arg):
    print(arg[0])
    print(arg[1])
    print(arg[2])
print_details("steewo",100,"thrissur")

# *arg ==> tuple aayittaanu accept cheyyuka

# ithil steewo ,100, thrissur enthaanennu convey cheyyunnilla(name: steewo, roll:100) thats why we use  **arg