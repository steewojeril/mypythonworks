lst=[10,20,30,40,50,60,70,80,90,100]
# 10**1 ,20**2, 30**3, .....10**10
count=1
for i in lst:
    res=i**count
    print(res)
    count+=1
    