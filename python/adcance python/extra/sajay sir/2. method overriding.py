# suppose child new phone vedichu
# so nth cheyyum ennu vachal, parent nte 'phone' method ne child override cheyyan poovaanu
#eppozhaanu override cheyyunnath :-
# child nu child ntethaayittulla implimentation detail venamenkil, override cheyyam

class Parent:  #parent nte kayyil phone car ind
    def phone(self):
        print("redmi note 7")
    def car(self):
        print("ertiga")

class Child(Parent):
    def phone(self):
        print("poco m2 pro")

ch=Child()
ch.phone() # here parent nte 'phone method ne child override cheyyum'
ch.car()   # here child nu car illa. so parent nte work aakum since it inferits parent class