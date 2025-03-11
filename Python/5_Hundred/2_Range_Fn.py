# Range Function with For Loop

# Range Function
for number in range(1, 11):
    print(number)

# Range Function with Step
for number in range(1, 11, 2):
    print(number)

# Question: Calculate the sum of all the numbers from 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)

for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(str(num) + '\n')
