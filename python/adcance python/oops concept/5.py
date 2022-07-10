# class employ
# employee name, id, designation, salary , company name
# create 3 employ data

class Employ():
    def setvalue(self,e_name,id,desig,salary,c_name):
        self.e_name=e_name
        self.id=id
        self.desig=desig
        self.salary=salary
        self.c_name=c_name
    def printvlaue(self):
        print(self.e_name,self.id,self.desig,self.salary,self.c_name)
e1=Employ()
e1.setvalue('steewo',19,'web developer',100000,'luminar')
e1.printvlaue()


e2=Employ()
e2.setvalue('siva',20,'web developer',100000,'luminar')
e2.printvlaue()


e3=Employ()
e3.setvalue('tinu',21,'web developer',100000,'luminar')
e3.printvlaue()