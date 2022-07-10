# map
# filter

#map- to do mapping
# to do an operation for each element in a list
# eg:
# lst=[1,2,3,4]  ==> f(x) ==> [1,4,9,16]  (operation is square)

# syntax:
# variable_name=list(map(argument1,argument2))
# argument1 ==> function
# argument2 ==> iterable(from which file we want to do the operation)


# to do square of each element
lst=[1,2,3,4,5,6,7,8,9,10]
def square(num):
    res=num**2
    return res
data=list(map(square,lst))
print(data)

# or
# data=list(map(lambda num:num**2,lst))





# filter- to do a filter for a given condition
# to find even numbers lst=[1,2,3,4] f(x)==> [2,4]
# to find vowel characters [a,c,e] f(x) ==> [a,e]

# syntax:
# variable_name=list(filter(argument1,argument2))
# argument1 ==> function
# argument2 ==> iterable(from which file we want to do the operation)

lst1=[1,2,3,4,5,6,7,8,9,10]
def even(num):
    return num%2==0
data1=list(filter(even,lst1))
print(data1)
# or
# data1=list(filter(lambda num:num%2==0,lst))