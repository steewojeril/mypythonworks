import re
s="jbjjjfjbkgjbjfj"
matcher=re.finditer('j',s)

count=0
for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print("count",count)