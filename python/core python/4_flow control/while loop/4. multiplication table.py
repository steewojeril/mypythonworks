# multiplication table of a given number upto 10
# eg : 2*1=2
num=int(input("enter number"))
i=1
while(i<=10):
    res=i*num
    print(i,"x",num,"=",res)
    i+=1