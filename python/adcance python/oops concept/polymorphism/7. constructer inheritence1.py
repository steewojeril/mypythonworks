# constructer inheritence(single inheritence)

# class person <<< name age place
# class student <<< roll dep college
# student inherit person
# saadha pole cheythatt(using method) thaazhe ulla steps cheyth nokk

# method ne constructer aaki matuka
# child class nte method nte akath type arguments of parent class
# for calling:-
#  child class nte method nu akath ==> using super().__init__(arguments of parent class )
class Person:
    def __init__(self,name,age,place):# this is a constructer
        self.name=name
        self.age=age
        self.place=place
    def printp(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def __init__(self,name,age,place,roll,dep,college):
        super().__init__(name,age,place)
        self.roll=roll
        self.dep=dep
        self.college=college
    def prints(self):
        print(self.roll,self.dep,self.college)

st=Student("steewo",24,"thrissur",42,'civil','christ')
st.prints()
st.printp()
print(st.age) # if you want to print only age