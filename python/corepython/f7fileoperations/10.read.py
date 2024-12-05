# calculate each country count
f=open("C:/Users/steew/Downloads/customer","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    if data[-1] not in dic:
        dic[data[-1]]=1
    else:
        dic[data[-1]]+=1
print(dic)

