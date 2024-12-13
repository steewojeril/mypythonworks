'''
Recursion is a programming technique where a function calls itself .
It allows a problem to be broken down into smaller, with a base case to terminate the recursive calls.  
eg: 3!. 
suppose fn knows that 3! is 3*2!. but it doesnt know 2! so it calls itself to find 2! first
but here also 2!=2*1!  .... and finally 1* 0!. 
it has to find 0! which is 1  
and then it calculates 
1*0! (1*1)
2*1! (2*1),
3*2! (3*2) ==> 6

'''
# FACTORIAL
# n*n! ==> n * fn(n-1) limit:up to n=0
def fact(n): # step2 . setting limit
    if n == 0:
        return 1 
    return n* fact(n-1)   #step1
print("factorial is",fact(4))
# ...............................................
# SUM OF N NUMBERS
# n+(n-1)  ==> n + fn(n-1) limit: up to n=0
def sum(n): # step2 . setting limit
    if n == 0:
        return 0
    return n+sum(n-1)
print("sum of n numbers",sum(2))
# ..............................................
# nth fibnoci number
# fibnoki of nth number is fibn(n-2)+ fibn(n-1) 
# limit: up to fibn(2-2)+fibn(2-1) ie fibn(0)+fibn(1) ,ie 0.1
def fib(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    return fib(n-2)+fib(n-1)
print("nth fibnocci number",fib(8))

# .....................
# sum of the digits of an integer
# n%10 + n//10%10 ==> n%10 + fn(num//10) 
# limit: up to n==0 which is 0
def sum_dig(n):
    if n==0:
        return 0
    return n%10 +sum_dig(n//10)
print("sum of digit",sum_dig(4567))
# .............................................
# Count the Digits of a Number
# count + 
def dig_count(n):
    if n // 10 == 0:  # Base case: single-digit number
        return 1
    else:
        n = n // 10  # Reduce the number by removing the last digit
    return 1 + dig_count(n)  # Add 1 for the current digit and recurse
print("digit count",dig_count(1000))