class Parent:  #parent nte kayyil phone car ind
    def phone(self):
        print("redmi note 7")
    def car(self):
        print("ertiga")

class Child(Parent):  # child parent ne inherit cheyyunnu
    pass

ch=Child()
ch.phone()  # child ntel 'phone' illa. but call cheyyumbo inheritence property vazhi parent nte 'phone' work aavum
ch.car()
