# 1. how to define
tu=()
tu1=tuple()

'''
Use case: fast iteration bcoz immutable,so eay for python to optimize memmory.
(datastructure: Array(fixed size))

# difference between list and tuple <<<
list is mutable
tuple is imutable
'''
tu=(1,1,2,6)
print(tu)

# only 2 mtds 

print(tu.count(1))  # to count given element repetitions
print(tu.index(6)) # to find the index of given element

# .............................
tuple1 = [(1, 'a'), (2, 'b')]  
for num, alph in tuple1:
    print(num , alph)