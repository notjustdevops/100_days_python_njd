from art import logo
from replit import clear
import random

print(logo)
print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

EASY_LEVEL = 10
HARD_LEVEL = 5
game_over = False

def game():
    random_number = random.randint(1, 101)
    print(random_number)
    if guess_attemt == random_number:
        print("You guesse the number!")


while not game_over:
    if difficulty == "easy":
        attemts = EASY_LEVEL
        print(f"You have {attemts} remaining to guess a number.\n")
        guess_attemt = input("Make a guess: ")

    elif difficulty == "hard":
        attemts = HARD_LEVEL
        print(f"You have {attemts} remaining to guess a number.\n")
        guess_attemt = input("Make a guess: ")
    else:
        print(f"Your input isn't valid. Try again.")
        exit()

game()