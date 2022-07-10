# if more than 1 condition
# syntax
# [print if condition else print range]
# in list comprehension 'elif 'is not supported
# [print if condition 1 else print if condition 2 else print



# from 1 to 50
# if even <<< square
# if odd <<< cube

lst=[i**2 if i%2==0 else i**3 for i in range(1,51)]
print(lst)
