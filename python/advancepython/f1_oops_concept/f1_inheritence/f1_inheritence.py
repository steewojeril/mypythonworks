# inheritance 
# child can access mtds and attributes of parent

# parent = super class = base class    ==>The class whose properties and methods are inherited.
# child  = sub class  = derived class  ==>The class that inherits from the parent class. It can use or override the parent class's properties and methods.

# single inheritence
class A:
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")
class B(A):
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")

b=B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()

# Multiple inheritence >>  inherit more than one class
# for this we need min 3 class in total

class A:
    def feature1(self):
        print("feature 1 working")
class B:
    def feature2(self):
        print("feature 2 working")
class C(A,B):
    def feature3(self):
        print("feature 3 working")
c=C()
c.feature1()
c.feature2()
c.feature3()

# multilevel inheritence << a class inherits from a class that is already a subclass of another class.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def play(self):
        print("Puppy plays")

puppy = Puppy()

# Accessing methods from all levels of inheritance
puppy.speak()  # Inherited from Animal
puppy.bark()   # Inherited from Dog
puppy.play()   # Defined in Puppy class


# Hierarchical Inheritance  << multiple subclasses inherit from a single parent class.
class A:
    def feature1(self):
        print("feature 1 working")
class B(A):
    def feature2(self):
        print("feature 2 working")
class C(A):
    def feature3(self):
        print("feature 3 working")
b=B()
c=C()
b.feature1()
b.feature2()

c.feature1()
c.feature3()
