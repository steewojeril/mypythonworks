#worcount programme using dictionary
# word count  <<< how many times each word repeat (not the total count)
line='cat rat bus cat car car rat bus car car bus cat'  #line of data
# step 1 : convert line of data into word by word data  <<< split function
data=line.split(' ') #we are splitting by space
print(data) # we get list ['cat', 'rat', 'bus', 'cat', 'car', 'car', 'rat', 'bus', 'car', 'car', 'bus', 'cat']
# step 2 : create empty dictionary
# step 3 :check each word from the list is present in dic
# if not present  word=1  add to dictionary
# if present incriment by 1
dic={}
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)

for i in dic:
    print(dic[i])

