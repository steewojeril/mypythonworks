# do word count of file word data
f=open("word data", "r")
dic={}
for i in f: # iterating each line in file
    data=i.rstrip("\n").split(' ')

    for i in data: # each element in list 'data'    # means at first, first element in first line' and so on # if this for loop is outside the above for loop,we only get data of last line(if not understsand just give "print data" inside and then ouside the above for loop. and see the difference
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
for i in dic:
    print(i,",",dic[i])

#another mtd to print key-value pair in

# for k,v in dic.items():
#     print(k,",",v)
