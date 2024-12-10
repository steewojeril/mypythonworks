'''
DATA TYPES:
None
int float complex bool
string
list tuple set dictionary

note: string, int, tuple are immutable. we cant modify. if we try to do it will either error or it will allocate new memmory location

'''



# if 2 values are same , python uses only same location (in case of imutables(str,int,tuple))
a=5
b=5
print(f"id of a and b are{id(a),id(b)}")
# here id of both are same 
# but if we try to change one of its value id will chnage
b=1 #id of b will change now
print(f"id of a and b are{id(a),id(b)}")

