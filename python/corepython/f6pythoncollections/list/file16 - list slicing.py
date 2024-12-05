# list slicing
lst=[10,32,65,63,244,59,87,2,5]
print(lst)

print(lst[:])   # full list

print(lst[:7])  # start to 7      # lst[0], lst[1], lst[2], lst[3]
print(lst[3:])  # 3 to end
print(lst[::2]) #  print with 2 steps (10,65,...) . default value of step is 1
print(lst[3:8])  #lst[3, lst[4], lst[5], lst[6], lst[7]   #upper limit will not include like 'for' loop


# negative indexing 
print(lst[-1])  # 5
print(lst[-3])  # 87



print(lst[-3:]) # lst[-3] to end    (-3,-2-,1)
print(lst[:-5]) # start(10,32,) to lst[-6]  (-9,-8,-7,-6)       
print(lst[::-1]) #  to print in reverse order 
print(lst[-4:-1])  # 59, 87, 2
