# interview question
f=open("content", "r")
# to remove special character from the file
special='!@#$%^&*()_+~{}'

for i in f:
    data=i.rstrip("\n")
    string = ""
    for j in data:
        if j not in special:
            string+=j
    print(string)

