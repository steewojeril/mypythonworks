lst=[4,5,10,12,20]
# creat lst1[47,46,41,39,31]
lst1=[]
for i in lst:
    total=sum(lst) # if we use 'sum' instead of 'total' programme will not work
    lst1.append(total-i)
print(lst1)