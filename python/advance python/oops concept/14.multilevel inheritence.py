# multilevel inheritence << inherit by levels
# c enna class nu b ne inherit cheyyunnu but b enna class a ne inherit cheyyunnund
# so indirectly class a , class c ne inherit cheyyunnu

class A:
    def printa(self):
        print("insidde A")
class B(A):
    def printb(self):
        print("inside B")
class C(B):
    def printc(self):
        print("inside C")
ob=C()
ob.printc()
ob.printb()
ob.printa() # A, B-ne mathrame inherit cheyyunnullu. But B, A-ne inherit cheyyunnath karanam C, A-ne inherit cheyyunnu