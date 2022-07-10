# encapsulation:

# oru class eduthal
# athine assosiate cheythittulla data yeyum , athine operate cheyyunna mehods neyum oriu place il thanne ezhuthunnathine parayunnath

#  here employee class << data(name and id) and methods(setvalue , read value) single unit aayi ezhuthunnath
#  ithinu munn data members nammal outside the class aanu ezhuthiyirunnath

class Employee:
    def __init__(self):
        self.name="steewo"
        self.id=13
    def readvalue(self):
        print(self.name,self.id)
e1=Employee()
e1.readvalue() # we can access methods
print(e1.name,e1.id) # we can access data/variables


# data(variable) or methods nte access control cheyyan access modifiers und

# access modifiers:-
# public
# protected  _  ==> its just like a warning but it can be accessed from anywhere
# private   __

# by default all methods and data/variables are public
# public :  can access methods and data/variables from everywhere