# one class collects features of other class
# features << mtd,variables

# parent = super class = base class
# child  = sub class  = derived class

# inheritance <<< 'child collects' features of parent
# child can access mtds and attributes of parent
class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Student(Person):
    def setstudent(self,roll,dep):
        self.roll=roll
        self.dep=dep 
    def printstudent(self):
        print(self.name, self.age, self.place,self.roll,self.dep) # parent nte var child il use cheyyunnu
st=Student()
st.setperson("steewo",24,"thrissur") # parent nte mtd child use cheyyunnu
print(st.name)  # parent nte var child il use cheyyunnu
st.setstudent(101,"bigdata")
st.printstudent()


