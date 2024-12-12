from sample1 import *
# to run a python file  => python3 
data=add(10,20)
print(data)

data1=sub(20,10)
print(data1)

data2=mul(2,2)
print(data2)

data3=div(4,2)
print(data3)

import os
def is_package(directory):
    return '__init__.py' in os.listdir(directory)

# Check if the current directory is a package
current_directory = os.getcwd()
if is_package(current_directory):
    print(f"{current_directory} is a package.")
else:
    print(f"{current_directory} is not a package.")