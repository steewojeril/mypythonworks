
# globals()- to get all the global variables
#  we can change the global var without affecting the local variable
a=10 # global variable. 
def number():
    # x=a   # 1. we cant access the global a inside a fn
    x=globals()['a']  # 2.. we can access global variables from inside the fn
    globals()['a']=15
    a=8 # 1. local variable. it cannot be used outside. bcoz the scope of this variable is inside the fn
    print("a=",a,"x==",x)

number()
print("a=",a)