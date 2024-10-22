# Write a program to accept the cost price of a bike and display the road tax to be paid according to the
# following criteria :
#
#         Cost price (in Rs)                                       Tax
#         > 100000                                                  15 %
#         > 50000 and <= 100000                                     10%
#         <= 50000                                                  5%

cost=int(input("enter cost of bike"))
tax=0 #programme will work if this statement is not entered.But this the std mtd
if(cost>100000):
    tax=cost*0.15
    print("tax to be paid",tax)
elif(50000<cost<=100000):   #(cost<=100000 & cost>50000)   (cost<=100000 and cost>50000)
    tax=cost*0.10
    print("tax to be paid",tax)
else:
    tax=cost*0.05
    print("tax to be paid",tax)
