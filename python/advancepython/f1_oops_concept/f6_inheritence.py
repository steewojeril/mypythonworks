# inheritance 
# child can access mtds and attributes of parent

# parent = super class = base class    ==>The class whose properties and methods are inherited.
# child  = sub class  = derived class  ==>The class that inherits from the parent class. It can use or override the parent class's properties and methods.


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

