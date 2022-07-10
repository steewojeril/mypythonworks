# private variable

# private : cant access outside the class,can access inside the class
# here variable accesscode is a private thing of an employee so it should not be access by anyone
# so we are making accesscode variable as private

class Employee:
    def __init__(self):
        self.name="steewo" #public
        self.id=13 # public
        self.__accesscode=123 #privatte
    def readvalue(self):
        print(self.name,self.id)

    def readaccesscode(self):
        print(self.__accesscode)
e1=Employee()
e1.readvalue()
print(e1.name,e1.id)
# print(e1.__accesscode)  here we cant access the private variable directly
e1.readaccesscode()  # here we can access it only through a public method inside the class

# ithpole method um private aakkaam

# so private aakiyal
# only inside the class il mathrame visibilty ullu, vere oridathum use cheyyan pattilla