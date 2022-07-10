class A:
    def printa(self):
        print("inside claa A")

class B(A):
    def printa(self):
        print("inside class B")

ob=B()
ob.printa()  # here overriding will work(class B work aakum)


class A:
    def printa(self):
        print("inside claa A")

class B(A):
    def printa(self):
        print("inside class B")

class C(B):
    def printa(self):
        print("inside class C")

ob=C()
ob.printa()  # here overriding will work (class C work aakum)

# multilevel aayalum, ethaano last child class athanu work aavuka for mtd overriding