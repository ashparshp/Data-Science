import random

word_list = ['apple', 'banana', 'orange']

chosen_word = random.choice(word_list)
print(chosen_word)  # <-- Optional: Remove this in a real game

correct_letters = []
game_over = False

while not game_over:
    guess_letter = input("Guess a letter: ").lower()

    display = ""
    for letter in chosen_word:
        if letter == guess_letter or letter in correct_letters:
            display += letter
        else:
            display += "_"

    # If guessed correctly, add it to correct_letters
    if guess_letter in chosen_word:
        correct_letters.append(guess_letter)

    print("Current word:", display)

    if display == chosen_word:
        game_over = True
        print("You win!")
    else:
        print("Guess again!")