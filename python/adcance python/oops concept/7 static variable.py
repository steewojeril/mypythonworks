# static variable
# class luminar
# name roll age institution_name fees
# institution_name and fees are same

class Luminar:
    inst="luminar"
    fees=30000
    def setvalue(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age
    def printvalue(self):
        print(self.name,self.roll,self.age,Luminar.inst,Luminar.fees)

st1=Luminar()
st1.setvalue('siva',100,23)
st1.printvalue()

st2=Luminar()
st2.setvalue('tinu',101,25)
st2.printvalue()

st3=Luminar()
st3.setvalue('steewo',102,24)
st3.printvalue()


# instance <<inside mtd
# static << inside class