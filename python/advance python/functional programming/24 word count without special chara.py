#do word count without any special character
f=open("content", "r")
# to remove special character from the file
special='!@#$%^&*()_+~{}'
string = ""
for i in f:
    data=i.rstrip("\n")
    for j in data:
        if j not in special:
            string+=j
# word count
dic={}
data1=string.split(' ')

for i in data1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)



