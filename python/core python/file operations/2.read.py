# to read data of file sample1
# right click on file <<< copy path or reference <<< copy absolute path of file as argument1
# C:\Users\steew\PycharmProjects\pythonProject\file operations\sample1(/ this slash should be used if using windowa
# if the file and the python file are in same package just type file name(sample1)
f=open("sample1", "r")
print(f) # will not get output

# to get the output:-
for i in f:  #for loop is to iterate each line
    print(i)