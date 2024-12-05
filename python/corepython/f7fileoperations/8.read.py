# age above 50 and india <<< fname,lname,age,proof
f=open("C:/Users/steew/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
    if(data[3]>'50') and (data[-1]=='india'): #(data[5]=='india'):IndexError: list index out of range(bcoz in this file some data is missing thats why error
        print(data[1:5])