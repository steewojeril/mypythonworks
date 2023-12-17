
# oru function nte value vere function il use cheyyan pattilla ('value' aanu not variable)
# advantage(self) :  we can use args of a mtd in other mtds of particular cls or its child clses
class Person:
    def setvalue(self,name,age,place):
        self.name=name  # what happens here << 'name' enna argument ne 'self.name' enna instant argument aakki maatunnu.
        self.place=place  
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)

pe1=Person()
pe1.setvalue('anu',26,'kochi')
pe1.printvalue()

pe2=Person()
pe2.setvalue('raju',26,'kollam')
pe2.printvalue()

pe3=Person()
pe3.setvalue('arun',26,'thrissur')
pe3.printvalue()