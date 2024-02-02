'''   
_____________
   /      _      \
   [] :: (_) :: []
   [] ::::::::: []
   [] ::::::::: []
   [] ::::::::: []
   [] ::::::::: []
   [_____________]
       I     I
       I_   _I
        /   \
        \   /
        (   )   -cfbd-
        /   \
        \___/
'''

print("\nWelcome to Treasure Island. Your mission is to find the treasure.\n")

left_or_right = input('You\'re at the cossroad. Choose "Left" or "Right"?\n').lower()
if "left" in left_or_right:
    swim_or_wait = input('\n"Swim" or "Wait"?\n').lower()
else:
    print("Fall into a hole. Game Over.\n")
    exit()

if "wait" in swim_or_wait:
    which_door = input('\nWhich door: "Red", "Blue", "Yellow"?\n').lower()
else:
    print("Attacked by trout. Game Over.")
    exit()
if "red" in which_door:
    print("Burned by fire. Game Over.\n")
    exit()
elif "blue" in which_door:
    print("Eaten by beasts. Game Over.\n")
    exit()
elif "yellow" in which_door:
    print("You Win!")
    exit()
else:
    print("Game Over.")