# interview question
# read a string
# add and print new string with consonents of first string
string1=input("enter the string")
string2=""
vowels='aeiouAEIOU'
for i in string1:
    if i not in vowels: # means i should not be present in vowels. if this condition is true add that i in to the new string
        string2+=i
print(string2)