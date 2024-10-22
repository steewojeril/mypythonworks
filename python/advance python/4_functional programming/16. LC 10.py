# 1 to 30
# if even <<< square
# if divisible of 5 <<< 0
# if odd <<< number

lst=[i**2 if i%2==0 else 0 if i%5==0 else i for i in range(1,31)]
print(lst)