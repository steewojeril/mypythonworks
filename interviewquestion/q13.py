
# interview question

# to remove special character from the file
f=open("/python/adcance python/functional programming/content", "r")

special='!@#$%^&*()_+~{}'

for i in f:
    data=i.rstrip("\n")
    string = ""
    for j in data:
        if j not in special:
            string+=j
    print(string)
