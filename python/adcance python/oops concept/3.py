
# oru function nte value vere function il use cheyyan pattilla ('value' aanu not variable)
# to make it instance argument(means oru function nte value vere function il use cheyyan) - self.argument
class Person:
    def setvalue(self,name,age,place):
        self.name=name  # what happens here << 'name' enna argument ne 'self.name' enna instant argument aakki maatunnu
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)
# advantage of doing this(self) : oru function nte value vere function il use cheyyan pattum
# # self <<< nammal kodukkuna argument ne instance argument aaki maataam

pe1=Person()
pe1.setvalue('anu',26,'kochi')
pe1.printvalue()

pe2=Person()
pe2.setvalue('raju',26,'kollam')
pe2.printvalue()

pe3=Person()
pe3.setvalue('arun',26,'thrissur')
pe3.printvalue()