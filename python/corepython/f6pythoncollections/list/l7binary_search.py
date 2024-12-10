# binary search

# 1. sort in the ascending order
# 2. declare 2 variable - low & upp
# 3. find mid-value  >>> (start index + end index)//2
# 4. check 3 conditions
    # if searching element > lst[mid]  >>>  low=mid+1
    # if searching element < lst[mid]  >>>  upp=mid-1
    # if searching element = lst[mid]  >>>  element found
# . check mid-value is greater or smaller than the entered value
# . change the start or end index accordingly

lst=[6,5,65,45,87,21,22,1]
lst.sort()  # lst=sorted(lst)
print(lst)
num=int(input("enter the number"))

low=0
upp=len(lst)-1
flag=0
while(low<=upp):
    mid=(low+upp)//2
    if(num<lst[mid]):
        upp=mid-1
    elif(num>lst[mid]):
        low=mid+1
    else: # num==lst[mid]
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")