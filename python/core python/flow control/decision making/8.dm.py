# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held Number of classes attended.
# And print percentage of class attended is student is allowed to sit in exam or not.

classes_held=int(input("no. of classes held"))
classes_attended=int(input("no. of classes attended"))

percentage=(classes_attended/classes_held)*100
print("your attendance percentage is",percentage)

if(percentage>=75):
    print("you are allowed to sit in exam")
else:
    print("you are not allowed to sit in exam")