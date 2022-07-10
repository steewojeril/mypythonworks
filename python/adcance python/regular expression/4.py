import re
s="abaabbbabaaaabab"

matcher=re.finditer('ab',s)

count=0
for i in matcher:
    count+=1
    print(i.start())  # index aayirikkum print cheyyuka
    print(i.group())  # group aayirikkum print aakuka
print("count",count)