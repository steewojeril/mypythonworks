'''
r-read
w-write
a-append
rb-read binary( for reading images)
rw= write binary

'''

rfile = open("/home/steewo/Documents/mypythonworks/python/corepython/f7fileoperations/sample1.txt","r")
print(rfile.readline().strip())   # to readd eachline
print(rfile.readline().strip())
rfile.close()
# or 
# with - no need to close
with open("/home/steewo/Documents/mypythonworks/python/corepython/f7fileoperations/sample1.txt","r") as rfile:
    with open("/home/steewo/Documents/mypythonworks/python/corepython/f7fileoperations/sample2.txt","w") as wfile:
        for i in rfile:
            wfile.write(i)
    
