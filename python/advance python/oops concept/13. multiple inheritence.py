# inherit more than one class
# for this we need min 3 class in total

class A:
    def printa(self):
        print("insidde A")
class B:
    def printb(self):
        print("inside B")
class C(A,B):
    def printc(self):
        print("inside C")
ob=C()
ob.printc()
ob.printb()
ob.printa()