# we can return multiple values in a fn, but it should have assigned variables for each .

def sub_sum(x,y):
    sum=x+y
    sub=x-y
    return sum, sub
sum, sub =sub_sum(10,5)
print(sum,sub)