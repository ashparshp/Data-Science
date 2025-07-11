# Subscripting
print("Hello"[0])

# String
print("123" + "345")

# Integer = Whole Number
print(123 + 345)

# Large Number
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean = True or False
print(True)
print(False)

# None = Absence of Value
print(None)

# print(len(123)) #Error

# Type Function
print(type(123))
print(type(3.14159))
print(type(True))
print(type("Hello"))
print(type(None))

# Type Conversion
print(int("123") + int("345") + 1)

# Error
# print(int("Hello")) #ValueError: invalid literal for int() with base 10: 'Hello'

# print("Number of Characters in your name:" + (len(input("What is your name? ")))) #TypeError: can only concatenate str (not "int") to str
print("Number of Characters in your name:" + str(len(input("What is your name? "))))