# accessing private variable through public method

class Employee:
    def __init__(self):
        self.name="steewo" 
        self.id=13 
        self.__accesscode=123 #private var
    def readvalue(self):  # public method
        print(self.name,self.id)

    def readaccesscode(self):
        print(self.__accesscode)
e1=Employee()
e1.readvalue()
print(e1.name,e1.id)
print(e1.__accesscode)  # error: here we cant access the private variable directly
e1.readaccesscode()  # here we can access it only through a public method inside the class
