# prime numbers from 1 to 100
for i in range(2,101):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,end=' ')

# or 
        
for i in range(2,101):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if flag==0:
        print(i,end=' ')