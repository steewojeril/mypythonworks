# key word arguments (double star arguments)

# def printvalue(*arg):
#     return arg
# print(printvalue("steewo",10,"civil")) # this will work

# but to assign key we use **arg
# if we use **arg it will act as dictionary

def printvalue(**arg):
    return arg
print(printvalue(name="steewo",roll=10,prof="civil"))  # output is like dictionary


def print_details(**arg):
    print(arg)
print_details(name="steewo",roll=100,place="thrissur")

# **arg ==> dictionary aayittaanu accept cheyyuka

