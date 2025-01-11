
# globals()- to access and change the global var without affecting the local variable
a=10 # global variable. 
def number():
    # x=a   # 2. we cant access the global 'a' inside a fn
    x=globals()['a']  #4. now we can use 'a' as local var
    globals()['a']=15 # Changing the global 'a' using globals()
    # global a # 3. to access the global var inside. it will give same value. but we cant use 'a' as local var anymore. 
    # bcoz now it became global(use same memoru loc) so give same value if print inside and outside the fn
    a=8 # 1. Local variable, which won't affect the global 'a' 
    print("Inside function: a =", a, "x =", x)
number()
print("Outside function: a =", a)
