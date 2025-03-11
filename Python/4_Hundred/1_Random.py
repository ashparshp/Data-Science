import random

# Generate a random floating-point number between 0.0 and 1.0
print(random.random())

# Generate a random integer between 1 and 10 (inclusive)
print(random.randint(1, 10))

# Generate a random floating-point number between 1 and 10 (inclusive of 1, exclusive of 10)
print(random.uniform(1, 10))

# Generate a random integer between 1 and 9 (inclusive)
print(random.randrange(1, 10))

# Randomly select an element from the list [1, 2, 8, 9, 10]
print(random.choice([1, 2, 8, 9, 10]))

random_number_0_to_25 = random.random() * 25
print(random_number_0_to_25)

# Heads or tails
coin_flip = random.choice(["Heads", "Tails"])
print(coin_flip)