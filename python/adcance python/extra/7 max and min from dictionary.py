# to find max and min from dictionary
dic1={'physics':56,'maths':65,'history':80}
print(dic1)

# print subject having lowest score

# print(min(dic1)) #this doesn't work
print(min(dic1,key=dic1.get))
print(max(dic1,key=dic1.get))