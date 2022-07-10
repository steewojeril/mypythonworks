st={10,12,15,16,20,25,25}
#to add elements in set <<< add function
st.add(50)
print(st) #{16, 50, 20, 25, 10, 12, 15}    50 is not added at last bcoz insertion is not preserved

#to add multiple elements in set <<< update function
# st.update([element1,element2,...])
st.update([51,21])
print(st)

# to calculate sum of set
# sum=0
# for i in st:
#     sum+=i
# print(sum)

print(sum(st))  # here we have 2 25 in set so only one 25 will be added bcoz duplicate value not supported

print(max(st))
print(min(st))

# length
print(len(st)) # actually it has 10 elements but bcoz the reason that set does not support duplicate values(there are two 25
# in this set)it will display 9
