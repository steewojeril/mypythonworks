'''
Method Overriding: The child class can override methods from the parent class. 
If needed, the parent class's method can be called using super().method_name().

# Constructor and Method Inheritance
 
Constructor Inheritance:
To call the parent class's constructor from a child class, we use super().__init__(...).or
directly by calling the parent constructor using ParentClass.__init__(self, ...).

Method Inheritance:
If the child class overrides a method, super().method_name() calls the parent method, 
'''

class Person:
    def __init__(self, name, age, place):  # Parent constructor
        self.name = name
        self.age = age
        self.place = place
    
    def printp(self):
        print("person:",self.name, self.age, self.place)

class Student(Person):  # Child class inheriting Person
    #Method Overriding
    def __init__(self, name, age, place, roll, dep, college): # ivide init ulla karanam ith call akum else parent nte call aakum
        super().__init__(name, age, place)  # Call parent 
        Person.__init__(self,name,age,place) # another way (note: include self)
        self.roll = roll
        self.dep = dep
        self.college = college
    
    def prints(self):
        print("Student:",self.roll, self.dep, self.college)

# Creating instance
st = Student("Steewo", 24, "Thrissur", 42, 'Civil', 'Christ')

# Calling methods
st.prints()  # Output: 42 Civil Christ
st.printp()  # Output: Steewo 24 Thrissur
print(st.age)  # Output: 24 (inherited from Person)


# In multiple inheritance, if multiple classes define __init__ methods, using super() ensures that the __init__ methods are called in the correct method resolution order (MRO). 
# You can view the MRO with the ClassName.__mro__ attribute.
print(Student.__mro__)
# if        class Student(Person,Employee):
# (<class '__main__.Student'>, <class '__main__.Person'>, <class '__main__.Employee'>, <class 'object'>)