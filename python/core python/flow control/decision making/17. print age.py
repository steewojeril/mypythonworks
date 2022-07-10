#read current year , current month, current date
# #read birth year, birth month, birth date
# print age

cur_year = int(input("enter current year"))
cur_month = int(input("enter current month"))
cur_date = int(input("enter current date"))
bir_year = int(input("enter year of birth"))
bir_month = int(input("enter month of birth"))
bir_date = int(input("enter date of birth"))

if(cur_month==bir_month):
    if(cur_date>=bir_date):
        print("age is", cur_year-bir_year)
    else:
        print("your age is", (cur_year-bir_year)-1)
elif(cur_month>bir_month):
    print("your age is", cur_year-bir_year)
else:
    print("your age is", (cur_year-bir_year)-1)

