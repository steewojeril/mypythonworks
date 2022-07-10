# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5

count=0
for i in range(1,5):
    count+=1
    for k in range(0,i):
        print(count,end=' ')
    for j in range(i+1,6):
        print(j,end=' ')
    print()