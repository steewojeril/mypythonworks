# 1
# 1 2
# 1 2 3
# 1 2 3 4

# print(i) to print same value in a row
# print(j) to print diff value in a row

# require 4 col and 4 row

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=' ')
    print()