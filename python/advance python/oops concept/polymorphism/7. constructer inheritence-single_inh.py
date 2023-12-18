# constructer inheritence(single inheritence)

# super()  refers parent
# super().mtd explicitly calls the method from the parent class regardless of any overrides .parent thanne call aakuum
# self.mtd calls the latest method.(if a mtd is overrided, that overrided cls will work)


# In Python, constructors aren't inherited by default. 
# bcoz __init__ calls when an object calls. in this example init of person will excecute only when person object is created
# so to excecute __init__ of superclass while creating object of child cls(or while initializing ini of child)
# super() is used
# syntax :  super().mtd_name(arguments of parent class )

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