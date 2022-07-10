# interview question
# find max temp of each district
# using dic
f=open("C:/Users/steew/Downloads/temper","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    dis=data[0] #storing current dis
    temp=data[1]  #storing current temp
    if dis not in dic:  # kannur 28  #kannur 30
        dic[dis]=temp
    else:
        old_temp=dic[dis]  #kannur is already in dic. so dic[dis]=28
        if (temp > old_temp):
            dic[dis]=temp
print(dic)


