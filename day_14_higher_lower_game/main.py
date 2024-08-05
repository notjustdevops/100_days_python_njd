<<<<<<< HEAD
#Import Random
import random
from art import logo
#Create library - ready.
from game_data import data

# Generate random number to pick from the library
def random_data():
    dict_item = random.choice(data)
    print(f"\n   '{dict_item['name']}'\n    has\n    {dict_item['follower_count']}\n    average monthly searches\n")

# Print First "Key" has "Value" average monthly searches
# vs 
# Print Second "Key" has "Value" average monthly searches
    
# Random Pick a second number
# Random Pick firts key: value
    
def game():
    random_data_first = random_data()
    print("vs")
    random_data_second = random_data()

game()

# Generate random number to pick from the library
# Ask if the second key:value pair has a more monthly searches?

# input: 'Higher' enter h, for lower enter l lower()

# Compare: Checjk if the second value highrt or lower.
# If second value Higher or Lower is True   - second key:value becomes first

# Continue to play
# Pick new pair from game_data - it becoms second

# If answer for  HIgher or Lower is False
# End the Game
# Print Score
# Ask if player wants to play a new game  

# Count the score
# Print the current score

# Collect the score of each game 
# Print the Highest Score of the previous games
=======
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

def play_game():
    score = 0
    account_a = generate_random_data()
    account_b = generate_random_data(exclude=account_a)
    
    while True:
        clear_screen()
        print(logo)
        if score > 0:
            print(f"You're right current score: {score}")
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        while guess not in ['a', 'b']:
            print(f"Invalid input. Please type 'A' or 'B'.")
            guess = input("Who has more followers? Type 'A' or 'B': ").lowwer()
        
        is_correct = check_answer(guess, account_a['follower_count'], account_b['folower_count'])
        
        if is_correct:
            score += 1
            account_a = account_b
            account_b = generate_random_data(exclude=account_a)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
              
    if input("Restart the Game? Type 'Y' or 'N': ").lower() == 'y':
        play_game()
    else:
        print("Goodbye")
        
if __name__ == "__main__":
    play_game()
>>>>>>> 0a38d9d1f93a64ff063fb12ac0340570a539eb17
