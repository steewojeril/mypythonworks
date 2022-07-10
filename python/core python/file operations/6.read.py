# to read a file from outside pycharm -
# name, last name, age
f=open("C:/Users/steew/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")  # this is like nested list
    fname=data[1]
    lname=data[2]
    age=data[3]
    print(fname,",",lname,",",age) #or data[1:4]
    # print(data[0:5:2]) 0,2,4  third value(2) is called 'step'
