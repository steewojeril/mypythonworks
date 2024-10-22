#read low lmt & upp lmt
# print sum of even numbers and odd numbers
# eg: 2 , 10
#  2+4+6+8+10
#  3+5+7+9

low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))
esum=0
osum=0
while(low<=upp):
    if(low%2==0):
        esum+=low
    else:
        osum+=low
    low+=1
print("sum of even numbers =", esum)
print("sum of odd numbers =", osum)