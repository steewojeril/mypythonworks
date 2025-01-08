# to add data in a file  to a list
# and print its sum

with open("/home/steewo/Documents/mypythonworks/python/corepython/f7fileoperations/numbers.txt","r") as f:
    ls=[]
    for i in f:
        ls.append(int(i.rstrip()))   
        # both removes whitespaces or whilespace characters(\n (new line) ,\t (tab)) by default(if nothing passes as argument) + given character
        # strip()  - removes from both ends.
        # rstrip()  - removes from the right end.
    print(ls)
    print(sum(ls))
    