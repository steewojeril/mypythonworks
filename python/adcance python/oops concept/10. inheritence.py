 # 2 class
 # person : name age place
 # student : roll, dep

 # print : name age place roll dep

class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Student(Person):
    def setstudent(self,roll,dep):
        self.roll=roll
        self.dep=dep
    def printstudent(self):  #we can avoid this function(give print statement inside setstudent)
        print(self.name, self.age, self.place,self.roll,self.dep)
st=Student()
st.setperson("steewo",24,"thrissur")
st.setstudent(101,"bigdata")
st.printstudent()