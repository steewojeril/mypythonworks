# fibnocci series
num=int(input("enter the number")) #3
first=0
second=1
print(first) #0
print(second) #1
for i in range(1,num-1): # (1,(3-1)) << (1,2) means ,only 1 time already 2 elements were printed. so you need to minus that count eg:
    third=first+second
    print(third)
    first=second
    second=third
