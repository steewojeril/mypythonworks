# to generate exception error

# to generate exception error if age less than 18
age=int(input("enter your age"))

if age>=18:
    print("eligible")
else:
    raise Exception("not allowed")