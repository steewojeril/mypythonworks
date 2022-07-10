# udate 50 to 100 in a tuple(tuple is imutable)
tu=(30,45,50,55,60,65,70,75,80)
print(tu)

lst=list(tu)

lst[2]=100


tu=tuple(lst)
print(tu)

