# constructer <<< object nte akath instance variable define/declare cheyyan vendi use cheyyunnath
# __init__ 
# object create cheyyumbo automatically ith call aakum
# class Person <<< name age place

class Person:
    def __init__(self,name,age,place): # this is a constructer
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
pe=Person("steewo",24,"thrissur")
pe.printvalue()
