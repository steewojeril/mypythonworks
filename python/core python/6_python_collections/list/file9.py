# creat a list having numbers(1 to 75)
# even lst  print
# odd lst   print

# sum
# even list sum
# odd list sum

lst=[]
for i in range(1,76):
    lst.append(i)
print(lst)

lst_odd=[]
lst_even=[]

for i in lst:
    if(i%2==0):
        lst_even.append(i)
    else:
        lst_odd.append(i)
print(lst_odd)
print(lst_even)

print("sum of list =",sum(lst))
print("sum of even list=",sum(lst_even))
print("sum of odd list=",sum(lst_odd))

