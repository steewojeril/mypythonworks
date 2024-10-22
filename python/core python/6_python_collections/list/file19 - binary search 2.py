# doupt
lst=[52,68,2,54,23,1,25,62,45,4,6,8,5]
lst.sort()
num=int(input("enter the number"))
start=0
end=len(lst)-1
mid=0
while(start<=end):
    mid=(start+end)//2
    if(num>lst[mid]):
        start=mid+1
    elif(num<lst[mid]):
        end=mid-1
    else:
        print("found")
        break
else:
    print("not found")