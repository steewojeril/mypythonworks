# 1. how to define
    # first method
tu=()
    # second method
    # can also define using list function
tu1=tuple()

                                    # Use case
# fast iteration bcoz immutable,so eay for python to optimize memmory ...(datastructure: Array(fixed size))



print(tu)

# 2. hetrogenous data supported or not
tu2=(10,10,5,'bigdata',10,555,True,'python')
print(tu2)
# it supports hetrogenous data

# 3. duplicated values is allowed or not
tu3=(10,101,15,15,'bigdata','bigdata',10,555,True,'python')
print(tu3)
# it supports duplicate values


# 4. insertion order is preserved or not
# insertion order is preserved(output order is same as that of input)

# 5. mutable or imutable (updation of data)
# imutable

# difference between list and tuple <<<
# list is mutable
# tuple is imutable

    # only 2 mtds 
# count
print(tu3.count(10))
# index
print(tu3.index(101))
# ..............................................
# advantage
# since it is immutable , iteration is fast compared to list
