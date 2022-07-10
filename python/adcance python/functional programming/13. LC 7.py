# 1 to 50
# even <<< square
# odd <<< print element

lst=[i**2 if i%2==0 else i for i in range(1,51)]
print(lst)