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