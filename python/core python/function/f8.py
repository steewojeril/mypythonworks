# factorial


# mtd1 >>> functions without argument and no return

def factorial():
    num=int(input("enter the number"))
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)

factorial()



# mtd2 >>> functions with argument and no return

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(fact)

factorial(5)




# mtd3 >>> functions with argument and return

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

res=factorial(5)
print(res)


