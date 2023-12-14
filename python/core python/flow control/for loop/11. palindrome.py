# palindrome
str=input("enter the word")
rev=str[::-1]
print(rev)
if (rev==str):
    print("palindrome")
else:
    print("not palindrome")

# slicing
# string='hello world'
# print(string[:4])
# print(string[::2])
# print(string[3:6])
# print(string[-8:-6])
# print(string[:])  # print full list
# print(string[5:1:-1]) #print reverse from 5 to 1
# print(string[::-1]) #print full list in reverse
    

    # or

strs=input("enter the word")
a=len(strs)
new=''
for i in range(a-1,-1,-1):
    new=new+strs[i]
if new==strs:
    print('palindrome')
else:
    print('not palindrome')


    