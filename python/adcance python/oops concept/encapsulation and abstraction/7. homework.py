# program using encapsulation

# create 2 class using encapsulation
# employ inherits person
# person nte ethenkilum variable private aakuka

class Person:
    def __init__(self):
        self.name="steewo" #public
        self._bank="canara bank"
        self.__pin=1234
    def printp(self):
        print("inside person")
        print(self.name)
        print(self._bank)
        print(self.__pin)
class Employee(Person):
    def __init__(self):
        Person.__init__(self)
    def printe(self):
        print("inside employ")
        print(self.name)
        print(self._bank)
        print(self.__pin)

e1=Employee()
e1.printp() # will get output
e1.printe() # will not work bcoz private variable pin is defined in another class(person). we cant inherit private variable