# so we are making readaccesscode method as private

class Employee:
    def __init__(self):
        self.name="steewo" #public
        self.id=13 # public
        self.__accesscode=123 #privatte
    def readvalue(self):
        print(self.name,self.id)
        self.__readaccesscode()
    def __readaccesscode(self):
        print(self.__accesscode)
e1=Employee()
# e1.__readaccesscode()  # here we cant access it directly from outside as it is a private method
e1.readvalue()  # but we can access it only through a public method inside the class