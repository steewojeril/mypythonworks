# class student
# name, roll no, dep, college
# create 3 student data
class Student:
    def setvalue(self,name,roll,dep,college):
        self.name=name
        self.roll=roll
        self.dep=dep
        self.college=college
    def printvalue(self):
        print(self.name)
        print(self.roll)
        print(self.dep)
        print(self.college)
st1=Student()
st1.setvalue('steewo',19,'civi','christ college')
st1.printvalue()

st2=Student()
st2.setvalue('siva',20,'civi','christ college')
st2.printvalue()

st3=Student()
st3.setvalue('tinu',21,'civi','christ college')
st3.printvalue()