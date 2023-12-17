import re

count=0
rule='[a-z]'  # [] means rule  "-" ==> to
# rule='[a-zA-Z]'   capital an lower
# rule='[0-9]'
# rule'[ ]'  space
matcher=re.finditer(rule,'abc @sabir123')   # 'abc @sabir123' ithinu akath  a to z evide und

for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print("count",count)
