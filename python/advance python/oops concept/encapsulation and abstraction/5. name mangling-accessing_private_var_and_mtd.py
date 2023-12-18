# name mangling - method to access private variable and method outside the cls

# syntax :
# object._classname__privatevariablename
# object._classname__privatemethodname

class Person:
    def __init__(self):
        self.name="steewo" 
        self.__pin=1234   #private var
    def printp(self):
        print("inside person")
        print(self.name)
        print(self.__pin)  
        self._Person__read_pin()
    def __read_pin(self):  #private mtd
        print(self.__pin)

class Employee(Person):
    def __init__(self):
        Person.__init__(self) # employee nte obj create cheyyumbo thanne parent inte init execute aakan vendi. illenil athint obj create cheyyandi varum
    def printe(self):
        print(self.name)
        print("inside employee")
        super()._Person__read_pin()
    
p=Person()
print(p._Person__pin)
p._Person__read_pin()
p.printp()


e=Employee()
print(e._Person__pin)
e._Person__read_pin()
e.printe()
