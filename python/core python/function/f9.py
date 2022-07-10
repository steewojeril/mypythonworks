# mtd1 >>> functions without argument and no return

def cube():
    num=int(input("enter the number"))
    cube=num**3
    print(cube)

cube()

# mtd2 >>> functions with argument and no return

def cube(num):
    cube=num**3
    print(cube)

cube(2)

# mtd3 >>> functions with argument and return

def cube(num):
    cube=num**3
    return cube

data=cube(3)
print(data)