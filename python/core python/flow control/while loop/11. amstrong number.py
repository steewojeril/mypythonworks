# amstrong number <<< sum of cube of a number equals to that number
#153 = (1^3)+(5^3)+(3^3)

num=int(input("enter the number")) #153
sum=0
n=num # ith koduthillel avasanam check cheyyumbo(sum==num) << always not amstrong << reason : num nte value maariyittundaakum bcoz of while
while(n>0):
    d=n%10 #3  #2
    sum+=(d**3) #3^3 + 5^3 + 1^3
    n=n//10 #15
if sum==num:
    print("amstrong")
else:
    print("not amstrong")