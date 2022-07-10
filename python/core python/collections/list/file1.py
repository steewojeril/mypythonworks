# lst

# 1. how to define
    # first method
lst=[] # empty list
print(type(lst)) # type of lst is list
    # second method
    # can also define using list function
lst1=list()

# 2. hetrogenous data supported or not
lst=[10,15,'bigdata','python',100,True]
print(lst)
# it supports hetrogenous data


# 3. duplicated values is allowed or not
lst=[10,10,15,'bigdata','python',100,True]
print(lst)
# it supports duplicate values


# 4. insertion order is preserved or not
lst=[10,10,15,'bigdata','python',100,True]
print(lst)
# insertion order is preserved(output order is same as that of input)

# 5. mutable or imutable (updation of data)
# list is mutable