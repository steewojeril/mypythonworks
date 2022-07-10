# sum of n numberes using *
def total(*arg): # here arg is now a tuple
    print(sum(arg))

total(1,2,3)


# or

def total(*arg): # here arg is now a tuple
    sum=0
    for i in arg:
        sum+=i
    return(sum)


print(total(1,2,3))
