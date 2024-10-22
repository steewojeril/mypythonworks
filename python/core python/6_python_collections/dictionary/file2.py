dic={"roll":101,"name":'vinay',"age":26,"dept":'bigdata',"marks":30}
print(dic)
# to collect only one value
# it is collected using corresponding keys  (important)

print(dic["marks"])


# to update the values in dictionary
dic["marks"]=100
dic["name"]='luminar'
print(dic)

# to print key and value
for i in dic:
    print(i,dic[i])

# or

for k,v in dic.items():
    print(k,",",v)

# to update marks 30 <<< 50
dic['marks']+=20
print(dic)

# to add key - value pair
dic['total']=150
print(dic)

# to delete key - value pair
del dic["roll"]
print(dic)

# to check key is present or not
print("name" in dic) # True or False


