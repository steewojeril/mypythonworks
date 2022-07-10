# def sub(n1,n2):
#     return n1-n2
# def div(n1,n2):
#     return n1/n2

# decorator : fn nte definition il oru change polum varuthand extra feature paranj kodukkan veendi aanu decorator use cheyyunnath

# argument of a decorator function should be a function (rule)
# it should contain a inner function
# no of parameters in inner function depends on the no of parameters on the function that we need to decorate (decorator cheyyenda function te akath ethra argument indo, athrayum argument aanu inner function nte akath vendath.

def dec_fn(fn): # fn=sub
    def inner_fn(n1,n2): #10,20
        if n2>n1:  #20>10
            (n1,n2)=(n2,n1)  #n1=20 n2=10
        return fn(n1,n2) #sub(20,10) ividannau actually sub call aavunnath. nerit sub call aavilla
    return inner_fn

@dec_fn #first come here when we call sub fn
def sub(n1,n2):
    return n1-n2
@dec_fn
def div(n1,n2):
    return n1/n2

print(sub(10,20))
print(div(2,10))