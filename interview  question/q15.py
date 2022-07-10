# sir

# interview question
lst=[1,3,4,5,4,3,2,7,8,9,3,4,2,1,9,10,11,12,15,13,12,11]
# output<<  [1,5,2,9,3,4,1,15]
# whenever series increase or increase print the number


for i in range(0,len(lst)):
    if(lst[i-1]<lst[i]>lst[i+1]) or (lst[i-1]>lst[i]<lst[i+1]):
        print(lst[i])

