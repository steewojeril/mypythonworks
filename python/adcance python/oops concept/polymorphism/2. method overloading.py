# method overloading
# same method name , different number of argument << ingane varunna conditon

#more number
class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
class Add1(Add):
    def sum(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+self.num3)

# in python no issue(python nte akath method overloading support cheyyilla)latest mtd aayirikkum work aavuka
# second sum aanu work aakum(class B nte)


# ob=Add1()
# ad1.sum(1,2)
# ith work aakilla bcoz latest mtd aanu work aavuka so aa sum il  3 variables und. nammal 2 ennam koduthittullu. so error kaanikkum

ob=Add1()
ob.sum(1,2,3) # here overloading will work
# ith work aakum





