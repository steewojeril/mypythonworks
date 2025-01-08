word_count={}
char_data=''
with open("/home/steewo/Documents/mypythonworks/python/corepython/f7fileoperations/word_data.txt","r") as file:
    for word in file:
        char_data+=word.lower().rstrip('\n.!')
    word_list=char_data.split(' ')
    for word in word_list:
        if word not in word_count:
            word_count[word]=1
        else:
            word_count[word]+=1
print(word_count)
