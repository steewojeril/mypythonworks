# give data from file 'customer'  (using constructer)
# Employee [id,fname,lname,age,prof,loc]
# also add that object data to a lst
class Employee:
    def __init__(self,id,fname,lname,age,prof,loc):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.loc=loc
    def printe(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,self.loc)
f=open("C:/Users/steew/Downloads/customer")
lst=[]
for i in f:
    data=i.rstrip("\n").split(",")
    id=data[0]
    fname=data[1]
    lname=data[2]
    age=data[3]
    prof=data[4]
    loc=data[-1]
    ob=Employee(id,fname,lname,age,prof,loc)
    # ob.printe()
    # print(ob.prof) #if we need only prof
    lst.append([ob.fname,ob.lname,ob.age,ob.prof])
print(lst)



