# regular expression package- ithinakath kore functions und(1000's of) but we need only one function- finditer
# finditer(argument1,argument2)
# argument1 ==> enthaano find cheyyanda pattern(eth pattern aano check cheyyendath)
# argument2 ==> eth string il  ninnaaanu check cheyyendath



# ab enna pattern ethra thavana string il varunnund
import re
s="abaabbbabaaaabab"

matcher=re.finditer('ab',s)       # matcher- just a variable 
# print(matcher)  ingane kodukkan pattilla


# for i in matcher:
#     print(i)
# inganyalla nammukk vendath . ehra thavana ab vannu ennanu vendath

count=0
for i in matcher:
    count+=1
print("count",count)


