#reverse

#

num=int(input("enter number"))  #153
res=0
while(num!=0):
    dig=num%10  #3  5  1
    res=(res*10)+dig  # (0*10)+3 =3     (3*10)+5=35
    num=num//10 # 153/10= 15
print(res)

