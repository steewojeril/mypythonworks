# read low and upp lmt
# print prime numbers between the limits

low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))

for i in range(low,upp+1):
    if(i>1):
        for j in range(2,i):
            if((i%j)==0):
                break
        else:
            print(i,end=' ')



# or
            
# read low and upp lmt
# print prime numbers between the limits

low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))
for i in range(low,upp+1):
    flag=0
    if(i>1):
        for j in range(2,i):
            if((i%j)==0):
                flag=1
                break
            
        if flag==0:
            print(i,end=' ')



