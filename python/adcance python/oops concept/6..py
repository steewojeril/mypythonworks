class Add:
    def setnumber(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def printvalue(self): # print cheyyan vere function kodukkunnath aanu std form
        print(self.num1+self.num2)
sum=Add()
sum.setnumber(40,50)
sum.printvalue()