import random

# Rock, Paper, Scissors Game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(game_images[user_choice])

computer_choice = random.choice(game_images)
print("Computer chose:")
print(computer_choice)

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == scissors:
    print("You win!")
elif user_choice == 1 and computer_choice == rock:
    print("You win!")
elif user_choice == 2 and computer_choice == paper:
    print("You win!")
elif computer_choice == rock and user_choice == 2:
    print("You lose!")
elif computer_choice == paper and user_choice == 0:
    print("You lose!")
elif computer_choice == scissors and user_choice == 1:
    print("You lose!")
elif computer_choice == game_images[user_choice]:
    print("It's a draw!")
else:
    print("You typed an invalid number, you lose!")