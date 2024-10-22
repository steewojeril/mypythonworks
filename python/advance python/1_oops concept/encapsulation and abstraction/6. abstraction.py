# abstracrion-shows only necessary details and hiding unnecessary deatails
# if a blueprint produces more than one child we use abstraction

# eg:vehicle produces car bike,etc
# vehicle have some common features
# benifits - hiding un necessary data, increase readability,reduce complexity


# how?
# inherit ABC class and use @abstractmethod decor for the mtds and the mtds should be empty  (abstract cls should have atleast 1 mtd)
# all abstract methods should be overrided in child cls and the implemetation is given inside those mtds

# so implementation details are hidden. we only know there is some common mtds.
# we are accessing the common mtds without knowing implementation
# here we know the common mtds(speed,capacity,tyre) of vehicle cls. implementation is hidden 

# ABC, abstractmethod -predefined abstract class, abstractmethod
from abc import ABC,abstractmethod
class Vehicle(ABC):  # abstract class
    @abstractmethod
    def speed(self):  # abstract method  (only declaration)
        pass        
    @abstractmethod
    def capacity(self): # abstract method  (only declaration)
        pass

    @abstractmethod
    def tyre(self):  # abstract method  (only declaration)
        pass
class Car(Vehicle):
    def speed(self):
        return 100
    def capacity(self):
        return 5
    def tyre(self):
        return 4
ob=Car()
print(ob.speed(),ob.capacity(),ob.tyre())

# ABC inherit, @decorator koduthillelum ith work aakum. 
# but ingane koduthal abstract cls inte rules/steps follow cheythillel warning varum.  
# eg: object create cheyyan pattila .bcoz athinte puurpose athalla
