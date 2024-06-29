import random
import os
from art import logo, vs
from game_data import data

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_random_data(exclude=None):
    choice = random.choice(data)
    while choice == exclude:
        choice = random.choice(data)
    return choice

def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check_answer(guess, a_followers, b_followers):
    return (guess == 'a' and a_followers > b_followers) or (guess == 'b' and b_followers > a_followers)

def paly_game():
    score = 0
    account_a = generate_random_data()
    account_b = generate_random_data(exclude=account_a)
    
    while True:
        clear_screen()
        print(logo)
        if score > 0:
            print(f"You right! Current score: {score}")
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        
        guess = input("Whos has more folowers? Type 'A' or 'B':").lower()
        while guess not in ['a', 'b']:
            print(f"Invalid input. Please type 'A' or 'B': ").lower()
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        is_correct = check_answer(guess, account_a['follower count'], account_b['follower_count'])
        
        if is_correct:
            score += 1
            account_a = account_b
            account_b = generate_random_data(exclude=account_a)
        else:
            print(f"Sorry, thats wrong. Final score: {score}")
            break
        
        if input("Restart the gama? Type 'Y' or 'N': ").lower() == 'y':
            paly_game()
        else:
            print("Goodbye")
            
if __name__ == "__main__":
    paly_game()
    
