import random

word_list = ['apple', 'banana']

choosen_word = random.choice(word_list)
print(choosen_word)

placeholder = ""
word_length = len(choosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)





guess_word = input("Guess a letter: ").lower()
print(guess_word)

display = ""

for letter in choosen_word:
    if (letter == guess_word):
        display += letter
    else:
        display += "_"

print(display)