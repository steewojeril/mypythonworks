string="steewojeril"
ch_word="lit"
dic={}
res=""
for char in string:
    if char not in dic:
        dic[char]=1
    else:
        dic[char]+=1
for char in ch_word:
    if char in dic:
        if dic[char]>0:
            dic[char]-=1
            res+=char
        else:
            break
    else:
        break
print(res==ch_word)