                                    # Use case
# faster insertion, lookup, deletion, ...(datastructure: Hash table)


# 1. how to define
# st={} empty curly bracket {} <<< it will read as dictionary
# if we add values in curly bracket eg: {1,2,3} <<< it will read as set (bcoz dictionary is a key-value pair, so if
# we are not giving key-value pair it will read as set)

# 1. how to define
st=set()  #define using list function
st1={1,23,2}


# does not support duplicate values


print(dir(set)) 
st={1,2,3,4,5}
print(st)
# cant directly edit. .set is not intended for that purpose.

st.add(88)  # to add element at end
print(st)

st.update([1,3,6,77]) # to add multiple elements 
print(st)


st.remove(77) # removes given element . but raises error if ele not present
print(st)
st.discard(77) # removes given element. dont raise error
print(st)

st.pop() # removes random element. raises error
print(st)




