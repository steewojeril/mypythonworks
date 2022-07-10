lst=[[101,'arun','k',26,'bigdata',1000],
     [102,'amal','p',27,'bigdata',1500],
     [103,'vishnu','e',24,'bigdata',1250],
     [104,'anoop','m',27,'bigdata',2000],
     [105,'hari','r',25,'bigdata',1750],
     [106,'vinay','s',28,'bigdata',1500]]
print(lst)

# to print each list in main list
for i in lst:
     print(i)

# to print only "name,lname, age, prof"
for i in lst:
     print(i[1],i[2],i[3],i[4])

# to print name,lname,age, prof, salary  of (age above 25)
for i in lst:
     if(i[3]>25):
          print(i[1], i[2], i[3], i[4],i[5])

# to print name,lname,age, salary  of (prof = bigdata)
for i in lst:
     if (i[4]=='bigdata'):
          print(i[1], i[2], i[3],  i[5])

# to print name,lname,age,prof, salary  of (salary above 1750 and age above 25)

for i in lst:
     if(i[3]>25) & (i[5]>1750):
          print(i[1], i[2], i[3], i[4], i[5])

#prin total salary
sum=0
for i in lst:
     sum+=i[5] # cant use sum function
print(sum)





