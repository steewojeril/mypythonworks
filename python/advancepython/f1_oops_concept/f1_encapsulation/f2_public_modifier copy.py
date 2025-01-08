# public_modifier.py

class Person:
    def __init__(self, name, age):
        self.name = name  # public attribute
        self.age = age    # public attribute

    def greet(self):  # public method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Example of public access:
person = Person("John", 30)
print(person.name)  # Accessing public attribute outside the class
person.greet()  # Accessing public method outside the class
