import re

# []	A set of characters
# \  to add special characters append this befoore the sp. char
# {}	Exactly the specified number of occurrences
# \d  digit
# \d{10}  exact 10 digits
#  ^  starts with
# [arn]	Returns a match where one of the specified characters (a, r, or n) is present
# [^arn]	(means except)Returns a match for any character EXCEPT a, r, and n
# [a-n]	Returns a match for any lower case character, alphabetically between a and n
# ?	Zero or one occurrences
# *	Zero or more occurrences
# +  (means upto)  One or more occurrences
# $	Ends with
# |  or
# ()	Capture and group
# \s	Returns a match where the string contains a white space character
# \S	Returns a match where the string DOES NOT contain a white space character
# \d	Returns a match where the string contains digits (numbers from 0-9)
# \D	Returns a match where the string DOES NOT contain digits
string='my phone number is 9567144225' # match phone number in this format
rule='\d{10}'
a=re.findall(rule,string)
print(a)

string1='my phone number is (999)-333-7775' # match phone number in this format
rule='\(\d{3}\)\-\d{3}\-\d{4}'
b=re.findall(rule,string1)
print(b)

string2='safjhldsjfl FY2021 Q1 was $5billion abcd FY2020 Q4 was $3biilion' # match the year and money and group it
rule = 'FY(\d{4} Q[1-4])[^\$]+\$(\d)'  # Updated regex pattern

c=re.findall(rule,string2)
print(c)
