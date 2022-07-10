# class person << name age
# child << place school
# student << roll dep college

# name age place dep college (school,roll venda)
# using multilevel inheritence

class Person:
    def setperson(self,name,age):
        self.name=name
        self.age=age
class Child(Person):
    def setchild(self,place,school):
        self.place=place
        self.school=school
class Student(Child):
    def setstudent(self,roll,dep,college):
        self.roll=roll
        self.dep=dep
        self.college=college
        print(self.name,self.age,self.place,self.dep,self.college)

st=Student()
st.setperson('steewo',24)
st.setchild('thrissur','holy angels')
st.setstudent(100,'civil','christ college')