# class

# syntax
# class Class_name:      (give first letter of Class name as capital)

# methods - class nte akath nammal define cheyyuna function ne parayunnath
class Person:
    def reading(self):
        print("reading books")
    def writing(self):
        print("writing a book")
#
# 'self' automatically varum
# here 'reading' , 'writing'  are methods
# self is an instance keyword . it refers to the current object
# we can create multiple methods


# to create an object

# object_name=class_name()
pe=Person()  #pe <<< object name
pe.writing() #reference -object nu purath nammal cheyyunna operations
pe.reading() #reference