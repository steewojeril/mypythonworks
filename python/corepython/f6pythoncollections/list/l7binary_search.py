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

lst = [6, 5, 65, 45, 87, 21, 22, 1]
num = int(input("Enter the number to search: "))

# Sort the list
lst1=sorted(lst)

start = 0
end = len(lst1) - 1

while start <= end:
    mid = (start + end) // 2  # Calculate mid in each iteration
    if num < lst1[mid]:
        end = mid - 1
    elif num > lst1[mid]:
        start = mid + 1
    else:
        ind=lst.index(lst1[mid]) #finding index in unsorted list
        print(f'Found {lst1[mid]} at index {ind}')
        break
else:
    print("Number not found")
