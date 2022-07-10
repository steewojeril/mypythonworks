# overriding
# refer 'method overriding sajay'
# same method name , same number of argument << << ingane varunna conditon

# python nte akath method overriding support cheyyum
# child class aayirikkum work aavuka(child class parent class ne override cheyyum)

class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("inside class A",self.num1+self.num2)
class Add2(Add):
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("inside class B",self.num1+self.num2)
ob=Add2()
ob.sum(15,20) # here overriding will work

