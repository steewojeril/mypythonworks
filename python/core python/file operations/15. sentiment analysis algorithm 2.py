# homework
f=open("comments", "r")
p=open("pos", "r")
n=open("neg", "r")

pos_lst=[]
for i in p:
    pos_lst.append(i.rstrip("\n"))

neg_lst=[]
for i in n:
    neg_lst.append(i.rstrip("\n"))

pos_dic={}
neg_dic={}
neu_dic={}
for i in f:
    data=i.rstrip("\n").split(' ')
    for j in data:
        if j in pos_lst:
            if j not in pos_dic:
                pos_dic[j]=1
            else:
                pos_dic[j]+=1
        elif j in neg_lst:
            if j not in neg_dic:
                neg_dic[j]=-1
            else:
                neg_dic[j]+=-1
        else:
            neu_dic[j]=0

pos_sum=0
neg_sum=0
neu_sum=0

def sum(sum,dic):
    for i in dic:
        sum+=dic[i]
    return sum

pos=sum(pos_sum,pos_dic)
neg=sum(neg_sum,neg_dic)
neu=sum(neu_sum,neu_dic)

total=pos+neg+neu

if total>0:
    print("overall response is positive")
else:
    print("overall response is negative")










