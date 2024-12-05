# set operations
st1={1,2,3,4,5,6,7,8,9,10}
st2={7,8,9,10,11,12,13,14,15}

# 1. Union - combine elements of both set (will not present duplicate elements)
st3=st1.union(st2)
print(st3)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}


# 2.Intersection - common elements from both sets
st3=st1.intersection(st2)
print(st3)   # {8, 9, 10, 7}


# 3.Difference - eg: A-B  <<< elements which present in setA and not present in setB
# element should present in A but should not present in B
st3=st1.difference(st2)
print(st3)  # {1, 2, 3, 4, 5, 6}

st3=st2.difference(st1)
print(st3)   #{11, 12, 13, 14, 15}