# print age

# gpt
# Read current year, month, and date
cur_year = int(input("Enter current year: "))
cur_month = int(input("Enter current month: "))
cur_date = int(input("Enter current date: "))

# Read birth year, month, and date
bir_year = int(input("Enter year of birth: "))
bir_month = int(input("Enter month of birth: "))
bir_date = int(input("Enter date of birth: "))

# Calculate age
age = cur_year - bir_year

# Adjust age if the birthday hasn't occurred yet this year
if (cur_month < bir_month) or (cur_month == bir_month and cur_date < bir_date):
    age -= 1

print(f"Your age is: {age}")
