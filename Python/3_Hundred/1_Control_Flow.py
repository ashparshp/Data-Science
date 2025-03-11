# Modulo: % operator returns the remainder of a division
10 % 3  # 1
10 % 2  # 0

# Even or Odd
number_to_check = int(input("What is the number you want to check? "))
if number_to_check % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Nested if statements
print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    # elif age >= 45 and age <= 55:
    elif 45 <= age <= 55:
        print("Everything is going to be okay. Have a free ride on us.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")