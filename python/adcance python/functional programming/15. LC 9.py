# to print number and print whether it is even or odd
lst=[(i**2,"even") if i%2==0 else (i,"odd") for i in range(1,31)]
print(lst)