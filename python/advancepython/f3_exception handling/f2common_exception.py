'''
###common exceptions:

ZeroDivisionError: Raised when dividing a number by zero.
ValueError: A ValueError occurs when you pass a value to a function or operation, and that value is of the correct type but inappropriate or invalid for the specific operation..

IndexError: Raised when trying to access an index that is out of range in a list.
KeyError: Raised when trying to access a key in a dictionary that does not exist.
TypeError: Raised when an operation is performed on an object of an inappropriate type.

'''
# ValueError
user_input = "abc"  # A string that cannot be converted to an integer
number = int(user_input)  # Trying to convert "abc" to an integer
# TypeError
a = "hello"
b = 5
print(a + b)  # Raises TypeError
