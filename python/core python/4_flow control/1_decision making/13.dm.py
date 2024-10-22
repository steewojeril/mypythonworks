# programme to read marks of 4 subjects out of 50 and print the following:
# 180 & above   A+
# 160-179      A
# 140-159      B+
# 120-139      B
# 100-119      C+
# 80-99        C
# below 99     failed

sub1=int(input("enter mark of subject 1"))
sub2=int(input("enter mark of subject 2"))
sub3=int(input("enter mark of subject 3"))
sub4=int(input("enter mark of subject 4"))
total=sub1+sub2+sub3+sub4
if(total>=180):
    print("your grade is A+")
elif(160<=total<=179):
    print("your grade is A")
elif(140<=total<=159):
    print("your grade is B+")
elif(120<=total<=139):
    print("your grade is B")
elif(100<=total<=119):
    print("your grade is C+")
elif(80<=total<=99):
    print("your grade is C")
else:
    print("failed")