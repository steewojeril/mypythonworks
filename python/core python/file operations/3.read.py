# to add data in a file  to a list
# and print its sum
f=open("numbers", "r")
lst=[]
for i in f:
    lst.append(i)
print(lst)
# output : ['100\n', '101\n', '102\n', '103\n', '104\n', '105\n', '106\n', '107\n', '108\n', '109\n', '110']
# \n means enteto remove that - rstrip function <<< to remove unwated things

# eg:
# line="hello\n"
# data=line.rstrip("\n")
# print(data)


# f=open("numbers","r")
# lst=[]
# for i in f:
#     lst.append(i.rstrip("\n"))
# print(lst)
# print(sum(lst))  <<< will not get output(string)

f=open("numbers", "r")
lst=[]
for i in f:
    lst.append(int(i.rstrip("\n")))
print(lst)
print(sum(lst))

