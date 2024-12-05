'''
In other programming languages like c++, java, there are 2 choices for passing an var to a function. 

    # pass by value
    when we pass a var to a fn by value, fn creates copy of the variable and will store in seperate memmory location. 
    so changing the value of copy doesn't change the original value

    # pass by reference
    when we pass a variable to a fn by reference, fn uses the same location of original object.
    so changing the object inside  the fn will affect the original

But in python there is no explicit method. so whether changes affect the object or not depends on 
whether the object is mutable or not.
    immutable (int, str, tuple)-> changes will not affect the orignal. bcoz saves in seperate memory loc. that is bcoz it is immutable
    mutable (list, set, dic) -> changes  will affect the orignal. bcoz it use the same memmory location . that is bcoz it is mutable
'''
# immutable (int)
def modify_val(x):
    x=10
a=5
modify_val(5)
print(a)  #5

# mutable (list)
def modify_list(ls):
    ls[0]='changed'

my_list=[1]
modify_list(my_list)
print(my_list)  # ['changed']