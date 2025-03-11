# Logical Operators
# Logical operators are used to combine conditional statements:
# and, or, not
# and: Returns True if both statements are true
# or: Returns True if one of the statements is true
# not: Reverse the result, returns False if the result is true

# Example
x = 5
print(x > 3 and x < 10)  # True

# Example
x = 5
print(x > 3 or x < 4)  # True

# Example
x = 5
print(not(x > 3 and x < 10))  # False

# Example
x = 5
y = 3
print(x != y)  # True
print(x == y)  # False
print(x < y)  # False
print(x > y)  # True
print(x <= y)  # False
print(x >= y)  # True

# Notes: Python does not have && and || operators