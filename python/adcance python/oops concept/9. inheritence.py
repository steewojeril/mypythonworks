# one class collects features of other class
# features << mtd,variables

# parent = super class = base class
# child  = sub class  = derived class

# inheritance <<< 'child collects' features of parent


class A: # parent class
    def printa(self,num1):
        self.num1=num1
        print("inside class A",self.num1)
class B(A): # child class
    def printb(self,num2):
        self.num2=num2
        print("inside class B",self.num2,self.num1)  #inherit cheythal parent class nakathe variable child class il access cheyyam

b=B() #b child class aanu. here parent class methods/variables access cheyyan parent class nu object indaakanamennilla(bcoz B inherits A)
b.printa(40)
b.printb(60)
# inheritence illenkil A kk vere object create cheyyendi varum (a=A()   a.printa())
