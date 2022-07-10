# create a file add content
# then copy this content to a new file(means write)
f=open("data", "r")
f1=open("data_copy", "w")
for i in f:
    f1.write(i)


