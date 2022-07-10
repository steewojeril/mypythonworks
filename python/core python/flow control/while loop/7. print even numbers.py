#to print only even numbers between upper lmt and lower lmt
low = int(input("enter number lower limit"))
upp = int(input("enter number upper limit"))
while (low <= upp):
    if (low % 2 == 0):
        print(low)
    low += 1