#1. create a list from element of a range from 1200 to 2000 with steps of 130  using list comprehension

#2.lst=[44,54,64,74,104]
# lst1=[50,60,70,80,110]  <<< output

# 3. create a list from element of a range from 1 to 15,
# print numbers whose square is greater than 50

#1
# lst=[i for i in range(1200,2001,130)]
# print(lst)

#2
# lst=[44,54,64,74,104]
# lst1=[i+6 for i in lst]
# print(lst1)

#3
# lst=[i for i in range(1,16) if (i**2)>50]
# print(lst)