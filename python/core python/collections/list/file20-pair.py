# # pair
# lst=[5,4,3,2,1]
# # read a num from console
# # print pairs of that number from the list
# # eg :6  <<<(4,2), (5,1)
# num=int(input("enter the number"))
# flag=0
# for i in lst:
#     for j in lst:
#         if((i+j)==num):
#             print("(",i,j,")",end=' ')
#         else:
#             flag=1
# if(flag>0):
#     print("no pair found")


# or (sir)
# to print only one pair
lst=[4,3,2,1]
num=int(input("enter the number")) #6
lst.sort() #[1,2,3,4]
low=0 #0
upp=len(lst)-1 #3
while(low<=upp): #0<=3   1<=3
    data=lst[low]+lst[upp]  #lst[0]+lst[3] =1+4 =5      2+4=6
    if(data==num): #false
        print("pairs are",lst[low],lst[upp])
        break
    elif(data>num): #false
        upp=upp-1
    else:
        low=low+1 #0+1 = 1