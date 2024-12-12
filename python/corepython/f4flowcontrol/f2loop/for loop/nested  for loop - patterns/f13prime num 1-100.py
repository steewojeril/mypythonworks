# prime numbers from 1 to 100
for i in range(2,101):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,end=' ')
print()
#  if we provide else to for loop , it works if entire loop works completely without break
# or 
        
for i in range(2,101):
    flag=1
    for j in range(2,i):
        if i%j==0:
            flag=0
            break
    if flag == 1:
        print(i,end=' ')
