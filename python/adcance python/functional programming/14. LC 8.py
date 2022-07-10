# 1 to 50
# even <<< element,square
# odd <<< element,print element

lst=[(i,i**2) if i%2==0 else (i,i) for i in range(1,51)]
print(lst)