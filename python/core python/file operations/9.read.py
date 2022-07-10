# calculate each prof count
# collect using dic
f=open("C:/Users/steew/Downloads/customer","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    prof=data[4]
    if prof not in dic:
        dic[prof]=1
    else:
        dic[prof]+=1
print(dic)


# f=open("C:/Users/steew/Downloads/customer","r")
# dic={}
# for i in f:
#     data=i.rstrip("\n").split(",")
#     if data[4] not in dic:
#         dic[data[4]]=1
#     else:
#         dic[data[4]]+=1
# print(dic)