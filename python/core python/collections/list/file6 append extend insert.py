# 1. append >>>  lst.append(element)
# 2. extend >>>  lst.extend([element1,element2,...])
# 3. insert >>>  lst.insert(index_number,element)


lst=[]
print(lst)

# to add single element to list >>> append function
# element is added at end

# lst.append(element)
lst.append(10)
print(lst)

lst.append('bigdata')
print(lst)

# to add multiple element to list >>> extend function

# element is added at end
# lst.extend([element1,element2,...])
lst.extend(['data',70])
print(lst)

# to add element in a particular position >>> insert function

# lst.insert(index_number,element)
lst.insert(0,55)
print(lst)
