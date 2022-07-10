# age above 50 fname lname, age, prof
f=open("C:/Users/steew/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
    for i in data: #we can avoid this for loop (already in there is forloop)
        if(data[3]>'50'): #(in file default is string )
            print(data[1],data[2],data[3],data[4])