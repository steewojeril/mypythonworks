# as we know, oru function nte args,var and vere function il use cheyyan pattilla ('value' aanu not variable)
# By using self, we can access attributes, args, and mtds of a class instance within other mtds of the same cls or its child clses.

class Person:
    def __init__(self, name, age):  # constructer # This is called automatically when creating an object
        self.name = name  # If we don't assign args like this, we cant use them in other mtds
        self.age = age
        print("Initialized")

    def greetings(self):
        print(f"I am {self.name}! I am {self.age} years old.")  
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

# Creating an object of the Person class
ranga = Person('Steewo', 19)

# Calling methods
ranga.greetings()  # Output: I am Steewo! I am 19 years old.
ranga.birthday()   # Output: Happy Birthday, Steewo! You are now 20 years old.

'''
Every time we create an object, a new space is allocated for it.
How much space? It depends on the number of variables.
Who is responsible? ==> The constructor.
'''