# accessing private method through public method

class Employee:
    def __init__(self):
        self.id=13 
        self.__accesscode=123 #private var
    def readvalue(self):  #public method
        print(self.name,self.id)
        self.__readaccesscode()
    def __readaccesscode(self): #private method
        print(self.__accesscode)
e1=Employee()
e1.readvalue()  # but we can access it only through a public method inside the class
e1.__readaccesscode()  # error: here we cant access it directly from outside as it is a private method