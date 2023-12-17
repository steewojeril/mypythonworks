import re

count=0
rule='[^abc]'  # ^ means except abc

matcher=re.finditer(rule,'abc @sabir123')   # 'abc @sabir123' ithinu akath except 'abc' evide und

for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print("count",count)
