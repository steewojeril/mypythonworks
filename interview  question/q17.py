# find whether the 'check_word' can be made using 'master_string
master_string="abbcddeghgggt"
check_word="get"
# hint : wordcount
# master_string nte count eduth vachu
dic={}
res=""
for i in master_string:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
for char in check_word:
    if char in dic:
        if dic[char]>0:
            dic[char]-=1
            res+=char
        else: #eggggg if count less than or equal to 0 ,we couldn't make the word
            break
    else: #tgzgg
        break
print(res==check_word)


# or  (my method)

match_char='ajgkbmdfvmdosgjegn'
ch='egg'


ch_word=''
for i in ch:
    for j in match_char:
        if i == j:
            ch_word+=i
            match_char=match_char.replace(i,"",1)
            break
if ch==ch_word:
    print(True)
else:
    print(False)



