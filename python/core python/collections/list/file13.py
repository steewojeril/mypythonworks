lst=[10,10,20,20,30,30,40,50,60,100,80,80,90]
# create new list from this list without duplicate elements

lst1=[]

for i in lst:
    if i not in lst1:  # means if i not present in lst1
        lst1.append(i)
    else:
        pass

print(lst1)


# another simple method is there useing 'set'
