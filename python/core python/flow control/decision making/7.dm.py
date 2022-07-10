# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary=int(input("enter salary"))
year=int(input("enter year of service"))
bonus=salary*0.05
if(year>5):
    print("your net bonus is",bonus)
    print("your salary is",bonus+salary)
else:
    print("you are not eligible for bonus")
