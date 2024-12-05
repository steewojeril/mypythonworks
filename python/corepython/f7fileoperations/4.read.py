# read numbers file and convert it into list and print sum
# print even lst and its sum
# print odd lst and its sum
f=open("numbers", "r")
lst=[]
lst1=[]
lst2=[]
for i in f:
    lst.append(int(i.rstrip("\n")))

print(lst)
print(sum(lst))

for i in lst:
    if(i%2==0):
        lst1.append(i)
    else:
        lst2.append(i)

print(lst1)
print("sum of even list",sum(lst1))
print(lst2)
print("sum of odd list",sum(lst2))