# decorator : to add a new fn to existing fn nte definition 
# existing fn il oru change polum varuthand extra feature paranj kodukkan veendi aanu decorator use cheyyunnath

# argument of a decorator function should be a function 
# it should contain a inner function
# no of parameters in inner function depends on the no of parameters on the function that we need to decorate (decorator cheyyenda function te akath ethra argument indo, athrayum argument aanu inner function nte akath vendath.

def dec_fn(fn): 
    def inner_fn(n1,n2): # same no of args sub fn have
        if n2>n1:  
            (n1,n2)=(n2,n1)  
        return fn(n1,n2) #sub(20,10) ividannau actually sub call aavunnath.
    return inner_fn

@dec_fn # 1.here python actually does     sub = dec_fn(sub)  means sub = inner_fn ==> not excecuting, jst preparing. so when we call sub() will execute the inner_fn()
def sub(n1,n2):
    return n1-n2
@dec_fn
def div(n1,n2):
    return n1/n2

print(sub(10,20))
print(div(2,10))