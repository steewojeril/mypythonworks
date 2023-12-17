# public protected private 

# private : can access only inside the class, cant access outside the class(means inherited class and direct aayi object. ennum paranj access cheyyanum pattilla)
# but through public functions and through data mangling we can access it outside the class

class Person:
    def __init__(self):
        self.name="steewo" #public
        self._bank="canara bank"  #protected
        self.__pin=1234   #private
    def printp(self):
        print("inside person")
        print(self.name)
        print(self._bank)
        print(self.__pin)   #can acces here
class Employee(Person):
    def __init__(self):
        Person.__init__(self)
    def printe(self):
        print("inside employ")
        print(self.name)
        print(self._bank)
        # self.printp()  #inherited class il ingane access cheyyam
        print(self.__pin)  #cant acces here  (bcoz private var cant access outside the class)

p1=Person()
print(p1.name)  
print(p1._bank)  
print(p1.__pin)  # error: will not work bcoz private var cannot be accessed outside the class
e1=Employee()
e1.printp()
e1.printe() # error: will not work bcoz private var can't access outside the cls(here inherited cls),private var pin is defined in another class(person).

