'''
Real-World Example:
Think of a bank account:
    -You have a private balance (like your bank balance).
    -You can't directly change the balance; you need to use functions like deposit() to add money or withdraw() to take money out. These functions control how your balance changes.
Why? So that no one can mess with your balance by directly setting it to an incorrect number.
Key Points:
-Encapsulation is like creating a safe box that holds data.
-You can control access to the data using public methods (like deposit() or withdraw()).
-This ensures the data is safe, and changes are made only in controlled ways.

'''

# access_modifiers_overview.py

'''
Access Modifiers in Python:

Python has three types of access modifiers for controlling the visibility and access to class variables and methods:

1. Public: Accessible from anywhere.
2. Protected (_): Meant for use inside the class and its subclassesits (just like a warning), but still accessible from outside
3. Private (__): Intended to be used only inside the class itself, and cannot be accessed from outside the class directly.

Public - Accessible everywhere.
Protected - Intended for internal use, but still can be accessed.
Private - Intended for internal use only and hidden from external access (can be accessed using name mangling).
'''
