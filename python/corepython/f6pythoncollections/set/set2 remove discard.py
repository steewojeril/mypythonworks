st={10,20,30,40,50,60,70,80,90,100}
print(st)
# to delete elements from a set >>> remove, discard
# remove >>>  have return type-give idea whether the element present or not
# discard >>> have no return type-no idea whether the element present or not


# remove
# st.remove(element)
st.remove(20)
print(st)

# discard
# st.discard(element)
st.discard(80)
print(st)

# if we try to remove an element which is not present in lst

st.remove(150)
print(st)     #give error message

st.discard(80)
print(st)     #no error message


