# logical operators

# AND  &
# OR   |
# XOR  ^

#AND
# Returns True if both operands are True. else false
# 0 0 0
# 1 0 0
# 0 1 0
# 1 1 1

num1=6
num2=4
print(num1&num2)
# output 4

#6     0 1 1 0
#4     0 1 0 0
#AND   0 1 0 0  - binary of 4

#OR
#Returns True if at least one operand is True.
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1

num1=5
num2=3
print(num1|num2)
# output 7

# 5  0 1 0 1
# 3  0 0 1 1
# OR 0 1 1 1 (7)


# XOR
#true when both are different, false when both are same
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0

num1=6
num2=7
print(num1^num2)
# output 1

# 6   0 1 1 0
# 7   0 1 1 1
# XOR 0 0 0 1