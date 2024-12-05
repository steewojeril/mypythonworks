# interview question
string1=input("enter the string")
string2=""
vowels='aeiouAEIOU'
for i in string1:
    if i not in vowels:
        string2+=i
print(string2)