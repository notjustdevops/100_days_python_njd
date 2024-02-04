from art import logo
from replit import clear
import random


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
GAME_OVER = False

# Function to check user's guess against actual answer.
def check_answer(guess, random_number, turns_qty):
    """Checks answer against guess. Returns the number of the turns remaining."""
    if guess > random_number:
        print("Too high.\n")
        return turns_qty - 1
    elif guess < random_number:
        print("Too low.\n")
        return turns_qty - 1
    else:
        print(f"You got it! The answer was {random_number}.\n")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS
    else:
        print(f"Oops. Try entering correct difficulty level.\n")
        

def play_game():
    print(logo)
    print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
    random_number = random.randint(1, 100)
    print(f"Psst. Your random number is: {random_number}")

    turns_qty = set_difficulty()
    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != random_number:
        print(f"You have {turns_qty} attemts remaining to guess the number.\n")

        # Let the user guess a number.
        guess = int(input(f"Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns_qty = check_answer(guess, random_number, turns_qty)
        if turns_qty == 0:
            print("You have run out of guesses, you lose.\n")
            return
        elif guess != random_number:
            print("Guess again.")

play_game()