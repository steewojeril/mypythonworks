# 1 1 1
# 2 2 2
# 3 3 3


# step 1: what to print (i  , j  ,*)
#         To print same value in a row >>> print(i)
#         To print diff value in a row >>> print(j)
#         To print same characters >>> print("that character")
# step 2: no of rows  (put this as range in i loop)


# step 3:apply logic to get what to type in j loop and get the shape

for i in range(1,4): #1
    for j in range(1,4):
        print(i,end=' ')  # end=' ' >>> to print in the same row with a space
    print() # to print in new line after each iteration  (to jump to the next line)