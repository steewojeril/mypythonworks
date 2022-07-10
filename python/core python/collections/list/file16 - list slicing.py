# list slicing
lst=[10,32,65,63,244,59,87,2,5]
print(lst)
print(lst[::-2]) #  to print in reverse order
print(lst[1:4]) # lst[1], lst[2], lst[3]   #upper limit will not include like 'for' loop
print(lst[3:8])  #lst[3, lst[4], lst[5], lst[6], lst[7]


print(lst[:7])  # start to 7      # lst[0], lst[1], lst[2], lst[3]
print(lst[3:])  # 3 to end
print(lst[:])   # full list

# negative indexing - start from end

# it start from -1  (not from o)

print(lst[-1])  # 5
print(lst[-3])  # 87

print(lst[-4:-1])  # 59, 87, 2

print(lst[-1:-4]) # blank (reverse order not possible)(only left to right

print(lst[-3:]) # lst[-3], lst[-2], lst[-1]
print(lst[:-5]) # start to lst[-6]  (-5+1 = -6)
