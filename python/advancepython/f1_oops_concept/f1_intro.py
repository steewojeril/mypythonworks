'''
**PARADIGM**: A way of thinking about how to structure and write code to solve problems.  
Python is a multi-paradigm language and supports:  
1. **Procedural Programming**: Code is organized into functions.  
2. **Functional Programming**: Examples include lambdas and list comprehensions.  
3. **Object-Oriented Programming (OOP)**:  
   - A way of designing programs using objects and classes.  
   - Object: A collection of attributes (data) and behavior (methods or functions that operate on that data).
   - **Class**: Serves as a blueprint for creating objects.  
   - **Reference**: Points to an object stored in memory.  
       - In Python, everything is an object, and variables act as references.  
       - Multiple variables can reference the same object, meaning changes made through one reference are reflected in all others. This is particularly important with mutable objects (e.g., lists, dictionaries).
'''

# Class Example

# Syntax for defining a class:
# class ClassName:  (Use PascalCase for class names in Python)

class Person:
    # Methods: Functions defined inside a class.
    def reading(self):
        print("Reading books")

    def writing(self):
        print("Writing a book")

# `self` is an instance keyword. It refers to the current object.

# Creating an object
# Syntax: object_name = ClassName()

pe = Person()  # both creates an object and assigns a reference to it.
# `pe` is a reference to a `Person` object stored in memory.
pe.writing()    # Output: Writing a book
pe.reading()    # Output: Reading books

# Alternative way to call a method explicitly:
# The method takes the object as an argument (this is what happens internally).
Person.writing(pe)  # Same as `pe.writing()`.
Person.reading(pe)  # Same as `pe.reading()`.

# Class: TV
# Object: Samsung, Lenovo, Sony (instances of the TV class)
# Reference: Variables like 'my_tv' that point to these objects
# Behavior (Methods): on, off, changing_channel (functions within the TV class)
'''
**Object-Oriented Programming (OOP) Concepts in Python:**

1. **Encapsulation**:
   - Bundles data (attributes) and methods (functions) into a single unit (class).
   - Access modifiers (`_`, `__`) can be used to control access, though Python does not strictly enforce them.
   - Example: Using getters and setters to control access to attributes.

2. **Inheritance**:
   - Allows a child class to inherit the attributes and methods of a parent class, promoting code reuse.
   - Python supports both single and multiple inheritance.
   - Example: A `Dog` class can inherit common behaviors like `eat()` from an `Animal` class.

3. **Polymorphism**:
   - Enables the use of a single interface for different underlying forms (data types or classes).
   - Example: Two classes, `Cat` and `Dog`, can each implement a `speak()` method. The behavior will differ based on the class.

4. **Abstraction**:
   - Hides implementation details while exposing only the essential features.
   - Achieved using abstract classes (via the `abc` module) or by defining methods intended to be overridden in subclasses.
   - Example: A `Shape` class can define a method `area()` to be implemented by its subclasses `Circle` and `Rectangle`.

Python's OOP features are easy to learn, allowing developers to write scalable, modular, and maintainable code.
'''


