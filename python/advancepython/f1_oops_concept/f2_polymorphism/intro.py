'''Polymorphism is one of the four fundamental principles of Object-Oriented Programming (OOP), 
along with encapsulation, inheritance, and abstraction. 

eG: as human we behave differently in different situation
same way , objects have multiple form
it allows the same method or function to behave differently based on the object it is acting on

Types of Polymorphism in Python
# method overloading <<< same method name , different number of argument << not supported in python
# method overriding  <<< same method name , same number of argument << supports in python
# Duck Typing : if it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck
# it focuses on an object's behavior, not its type.(object)
    The make_fly() function doesn't care about whether the object passed to it is a Bird, a Plane, or something else. 
    All it cares about is whether the object can "fly" (i.e., whether it has a fly() method).
'''
# duck typing

class Bird:
    def fly(self):
        print("Bird flies")

class Plane:
    def fly(self):
        print("Plane flies")

# Function that takes any object with a 'fly' method
def make_fly(flyable):
    flyable.fly()

# Creating instances
bird = Bird()
plane = Plane()

# These objects don't share a common parent class, but both have a 'fly' method
make_fly(bird)  # Output: Bird flies
make_fly(plane) # Output: Plane flies


# method overriding- it is a type of polymorphism
#when to use:-
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
ch.car()   # here child nu car illa. so parent nte work aakum since it inherits parent class

class A:
    def printa(self):
        print("mrthod1")
    def printa(self):
        print("method2")
ob=A()
ob.printa()
# inheritence onnum illenkil latest mtd aayirikkum work aavuka


