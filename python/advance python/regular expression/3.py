import re
s="abaabbbabaaaabab"

matcher=re.finditer('ab',s)

count=0
for i in matcher:
    count+=1
    print(i.start())  # inddex aayirikkum print cheyyuka
print("count",count)