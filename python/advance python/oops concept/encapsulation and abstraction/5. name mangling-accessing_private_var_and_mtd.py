# methods to access private variable and method

# name mangling

# syntax :
# object._classname__privatevariablename
# object._classname__privatemethodname

class Employee:
    def __init__(self):
        self.name="steewo" #public
        self.id=13 # public
        self.__accesscode=123 #privatte
    def setvalue(self,name,id):
        self.name=name
        self.id=id
    def readvalue(self):
        print(self.name,self.id)
        self.__readaccesscode()
    def __readaccesscode(self):
        print(self.__accesscode)

e1=Employee()
print(e1._Employee__accesscode)
e1._Employee__readaccesscode()