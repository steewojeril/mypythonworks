'''
Instance Variables:
   - Defined inside the `__init__` method.
   - These are specific to each object.

Class var/Static Variables:
   - Defined inside the class (outside the `__init__` method).
   - These are shared by all objects.
   - If we change a static variable using `ClassName.var`, it changes for all objects.
   - If we change a static variable using `self.var`, it creates or changes an instance-specific variable for that particular object.
'''

class Luminar:
    inst = "Luminar"  # Static variable
    fees = 30000      # Static variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def print_value(self):
        # Accessing instance variables and static variables
        print(f"Name: {self.name}, Age: {self.age}, Institution: {Luminar.inst}, Fees: {Luminar.fees}")

# Creating objects of the Luminar class
st1 = Luminar('Siva', 23)
st1.print_value()

st2 = Luminar('Steewo', 25)
st2.print_value()

# Accessing and modifying the static variable using an object reference (affects only this object)
st2.fees = 28000
print(f"Discounted fees for Steewo: {st2.fees}")

# Modifying the static variable for all objects
Luminar.fees = 26000
print(f"Discounted fees for all: {Luminar.fees}")  # Affects all except objects with instance-specific `fees`
print(f"Discounted fees for Steewo: {st2.fees}")   # Instance-specific value remains unchanged
