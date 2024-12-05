

#1. Find all of the numbers from 1-1000 that are divisible by 7
# lst=[i for i in range(1,1001) if i%7==0]
# print(lst)


#2. Find all of the numbers from 1-1000 that have a 3 in them

# lst1=[i for i in range(1,1001) if '3' in str(i)]
# print(lst1)


#3. Count the number of spaces in a string
string='Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
lst=[i for i in string if i==' ']
print(len(lst))


#4. Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
# string='Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
# vowels='aeiou'
# lst=[i for i in string if i not in vowels]
# print(lst)