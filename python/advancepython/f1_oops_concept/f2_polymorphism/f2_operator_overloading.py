'''
OPERATOR OVERLOA      D                                              DING:
allows you to define or modify the behavior of standard operators (like +, -, *, ==, [], etc.)
NOTE:
a+b    ==>   a.__add__(b)    #actually this is happening. __add__ is method inside int class 
'hello' + 'World'      ==> 'hello'.__add__('world')    __add__ is also in string class
print(a)  ==>  a.__str__()
'''
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1  # Marks for subject 1
        self.m2 = m2  # Marks for subject 2

    def printstud(self):
        print(self.m1, self.m2)

    def __add__(self, other):  # This is called when we use the + operator
        # Check whether the 'other' is an instance of the Student class
        if isinstance(other, Student):
            m1sum = self.m1 + other.m1  # Adding m1 marks
            m2sum = self.m2 + other.m2  # Adding m2 marks
            return Student(m1sum, m2sum)  # Return a new Student object with the sums
        return NotImplemented

    def __str__(self):  # Define the __str__ method to print the Student object correctly
        return f"Student(m1: {self.m1}, m2: {self.m2})"

# Example Usage
s1 = Student(10, 33)
s1.printstud()  # Output: 10 33

s2 = Student(10, 10)
s3 = s1 + s2  # This calls s1.__add__(s2)

print(s3)  # This calls s3.__str__() and prints the result
