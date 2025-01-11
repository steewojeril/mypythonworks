# squaring numbers - no dondition
lst = [i**2 for i in range(5)]
print(lst)

# squaring even numbers - one if dondition
lst = [i**2 for i in range(5) if i%2 == 0]
print(lst)

# checking odd or even - if else dondition
lst = [f"{i}-even" if i%2 == 0 else f"{i}-odd" for i in range(5)]
print(lst)

# Categorizing by range (negative, zero, positive) - We can't use elif directly,but can use nested if...else
numbers = [-5, 3, 0, 12, -2, 15]
categories = ['negative' if i<0 else 'zero' if i==0 else 'positive' for i in numbers]
print(categories)
