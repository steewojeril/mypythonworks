# 1. how to define
lst=[] # empty list
lst1=list()

'''
Use case: where sequene is required and mutable.
(datastructure: dynamic array)
'''



# methods-  
print(dir(list)) 


ls=[1,55,9]

ls[1]=32 # to edit the value of given index
print(ls)

ls.append(88)  # to add element at end
print(ls)

ls.extend([1,3,6,77]) # to add multiple elements 
print(ls)

ls.insert(0,0) # to add element at given index
print(ls)

ls.remove(77) # removes given element
print(ls)

ls.pop() # removes element of given index or last element 
print(ls)

ls.reverse() #to reverse a list
print(ls)

ls.sort(reverse=True) # to sort list in descending order. sort()-ascending order
print(ls)

ls.count(1)  # to count the element repetition
print(ls.index(9)) # to know the index of given element

ls.clear() #to remove all elements
print(ls)
