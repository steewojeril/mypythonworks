# filter odoo
lt=[('a',1),('b',2),('c',3),('d',4),('e',5),('f',6)]
# >> [[('a',1,'b',2)],[('c',3,'d',4)],[('e',1,'f',2)]]

filter=[]
for i in range(0,len(lt),2):
    if i==len(lt)-1:
        filter.append([lt[i]])
    else:
        s=slice(i,i+2)
        filter.append(lt[i:i+2])
print(filter)

# reduced line of code:

def filter_purpose(lt):
    filter1=[[lt[i]] if i==len(lt)-1 else lt[i:i+2] for i in range(0,len(lt),2)]
    return filter1
filter1=filter_purpose(lt)

print(filter1)


for i in filter1:
    print(i[0][0],i[0][1],end=" ")
    print(i[1][0],i[1][1],end=" ")
    print()

