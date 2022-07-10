# abstracrion
# vehicle << car bus bike
# car is not bus is not a bike. they all have some common features, but are not the same eg:milage, no. of tyres...
# inganulla general features ne programme cheyyumbol aanu aavashyam

# abstract class nakath abstract method ezhuthum . athinakath empty aayirikkum kodukuka(declaration matthram undakum, no contents.)
# ee class then parent class aake kore child class undaakkum. eennitt aa child class nakathaayirikkum athinte contents add cheyyuka

# then, abstract class nte object nammal create cheyyilla. boz it is actually empty. child class nte object aayirikkum create cheyyuka
#abstract parent class nteyum child class nteyum method name same aayathinal also same no. of arguments, ivide override cheyyum(means child class le method aayirikkum work aavuka)

# abstract class -  class having atleast one abstract method
# abstract method -  methods having only declaration

# benifits: presenting relevant data to user,we can hide unneccessary data ( here car,bike,bus only visible. vehicle is not visible to the user)

# ABC, abstractmethod -predefined abstract class, abstractmethod
from abc import ABC,abstractmethod
class Vehicle(ABC):  # abstract class
    @abstractmethod
    def speed(self):  # abstract method
        pass

    @abstractmethod
    def capacity(self): # abstract method
        pass

    @abstractmethod
    def tyre(self):  # abstract method
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
