# constructer inheritence(multiple inheritence)
# person [name,age,place]
# employ [id,dep,salary]
# student [roll,college]
# student inherit person and employ

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Employee:
    def __init__(self,id,dep,salary):
        self.id=id
        self.dep=dep
        self.salary=salary
class Student(Person,Employee):
    def __init__(self,name,age,place,id,dep,salary,roll,college):
        Person.__init__(self,name,age,place) # instead of super use class name (also give self)
        Employee.__init__(self,id,dep,salary)
        self.roll=roll
        self.college=college
    def prints(self):
        print(self.roll,self.college,self.name,self.age,self.place,self.id,self.dep,self.salary)
ob=Student("steewo",24,"thrissur",100,'civil',10000,1,'christ')
ob.prints()

# difference

# normal constructer
# just type __int__ instead of method
# call inside object

# constructer inheritence(single inheritence)
# upper().__init__(arguments)
# child class nte akath parent arguments kodukkuka
# call inside object

# constructer inheritence(multiple inheritence)
# parent.__init__(self,arguments)
# child class nte akath parent arguments kodukkuka
# call inside object

