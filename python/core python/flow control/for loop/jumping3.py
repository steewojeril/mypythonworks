# pass >>> it will do nothing
for i in range(1,51):  #1,2,3,.........23,24   25 will not be printed
    if(i==25):
        pass
    print(i)

# it will print from 1 to 50
# eg:even aanenkil onnum cheyyanda
for i in range(1,51):
    if(i%2==0):
        pass
    else:
        print(i**2)