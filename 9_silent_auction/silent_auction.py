from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)


def add_new_bid(name, bid):
    new_bid = {}
    new_bid['name'] = name
    new_bid['bid'] = bid
    print(f"new_bid check {new_bid}")
    

should_continue = True
while should_continue:
    name = input(f"What is your name? ")
    bid = int(input(f"Enter you bid $"))
    
    answer = input(f"Are there any other bidders? Type 'yes' or 'no'.\n")
    
    if answer == 'yes':
        print(add_new_bid)
        clear()
    else:    
        should_continue = False
        print("Now we'll make a calculation")


add_new_bid(name, bid)