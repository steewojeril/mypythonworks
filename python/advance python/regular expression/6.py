# basic rules

import re

count=0
rule='[abc]'  # [] means rule
# rules nte akath enth kodukkunnu athaanu rule

matcher=re.finditer(rule,'abc @sabir123')   # 'abc @sabir123' ithinu akath 'a' evede und 'b' evide und 'c' evide und

for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print("count",count)

# another example

import re

count=0
rule='[23]'  # [] means rule

matcher1=re.finditer(rule,'abc @sabir123')   # 'abc @sabir123' ithinu akath '2' evede und '3' evide und

for i in matcher1:
    count+=1
    print(i.group())
    print(i.start())
print("count",count)