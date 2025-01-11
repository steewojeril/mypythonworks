# map
# filter
# reduce
# these all take other functions as arguments 
squared = map(lambda x: x**2, numbers)

'''
MAP- Purpose: Applies a given fn to all items in an iterable and 
returns a new iterable (usually a map object) containing the results.

map(fn, iterable)

'''

# to do square of each element
lst=[1,2,3,4,5,6,7,8,9,10]
data=list(map(lambda num:num**2,lst))
print("map",data)

'''
FILTER- to do a filter for a given condition
Purpose: Filters elements from an iterable by applying a function that returns True or False for each element. 
the result will be the elements for which the fn returns True or False.

filter(fn, iterable)

'''
# even list
lst1=[1,2,3,4,5,6,7,8,9,10]
data1=list(filter(lambda num:num%2==0,lst))
print("filtered data",data1)

'''
REDUCE
The reduce() function applies the function to the first two elements of the iterable.
It then takes the result of that operation and applies the function again to the next element in the iterable.

from functools import reduce
reduce(fn, iterable, [initializer])
'''
from functools import reduce

numbers = [1, 2, 3, 4]
sum_with_initializer = reduce(lambda x, y: x + y, numbers, 10) #The initializer is 10, so the function starts with 10 as the first argument.
# 10+1+2+3+4
print("reduce",sum_with_initializer)  # Output: 20
