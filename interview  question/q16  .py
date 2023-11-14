lst=[('vinay',35),('arjun',35),('amal',65),('vipin',56),('anu',67)]
# find the student having higest mark and print that mark
marks=[]
for i in lst:
    marks.append(i[1])
maximum=max(marks)

for j in lst:
    if j[1]==maximum:
        print(j[0],maximum)

        # or  (this is effective method)
maximum=0
for n,m in lst:
    if m>maximum:
        maximum=m
        name=n
print(name,maximum)
