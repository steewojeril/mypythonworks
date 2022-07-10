# 1. how to define
# st={} empty curly bracket {} <<< it will read as dictionary
# if we add values in curly bracket eg: {1,2,3} <<< it will read as set (bcoz dictionary is a key-value pair, so if
# we are not giving key-value pair it will read as set)

# 1. how to define
st=set()  #define using list function
st1={1,23,2}

# 2. hetrogenous data supported or not
st2={10,15,'bigdata','python',100,True}
print(st2)
# it supports hetrogenous data

# 3.insertion order is preserved or not
# insertion order is not preserved

# 4. duplicated values is allowed or not
st3={2,3,4,True,'bigdata'}
print(st3)
# does not support duplicate values

st4={1,2,3,4,True,'bigdata'}
print(st4)  # here True will not print, bcoz set does not support duplicate values. as value of True is 1 and
# the set contains another 1, only one 1 will be displayed



# 5. mutable or imutable (updation of data)
# set is mutable