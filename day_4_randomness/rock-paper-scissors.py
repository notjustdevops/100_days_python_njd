import random

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

game_pictures = [rock, paper, scissors]

user_choise = int(input("\nWhat do you choose?\nType 0 for Rock, Type 1 for Paper, Type 2 for Scissors\nEnter your choise: "))
if user_choise >= 3 or user_choise < 0:
    print("You type an invalid number. You lose.")
else:
    print(game_pictures[user_choise])

    computer_choise = random.randint(0, 2)
    print(f"\n\nComputer chose:")
    print(game_pictures[computer_choise])


    if user_choise == 0 and computer_choise == 2:
        print("You win!")
    elif computer_choise == 0 and user_choise == 2:
        print("You lose!")
    elif computer_choise > user_choise:
        print("You loose!")
    elif user_choise > computer_choise:
        print("You win!")
    elif computer_choise == user_choise:
        print("It's a draw")