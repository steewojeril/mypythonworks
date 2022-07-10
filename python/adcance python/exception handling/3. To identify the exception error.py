# to identify the exception error -' exception' module
a=[1,2,3,4]
i=int(input("enter a index"))
try:
    print(a[i])
except Exception as e: # e is just a variable. this module is assigned to variable 'e'
    print("exception occured : ",e)