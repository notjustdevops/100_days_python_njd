from os import system, name
from time import sleep


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18},
        "cost": 1.5,
        },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24},
        "cost": 2.5,
        },
    "cappucinno": {
        "ingredients": {
            "water": 200,
            "milk": 100,
            "coffee": 24},
        "cost": 3.0,
        }
    }

def convert_menu_items():
    'E'.lower = MENU['']
    MENU["espresso"]
    MENU["latte"]
    return convert_menu_items
    
    
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    }

profit = 0


def print_report():
    print(f"\nWater: {resources['water']}ml\n",\
    f"Milk: {resources['milk']}ml\n",\
    f"Coffee: {resources['coffee']}g\n",\
    f"Money: {profit}\n")
    return resources


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    return clear


# TODO: 
# def calculate_profit():


# TODO 
# def check_resources_sufficient():
    

# TODO:
# def process_coins():

      
# TODO:
# def check_transaction():
# while True


# TODO: 
# The prompt should show every time action has completed, e.g. once the drink is dispensed.
# The prompt should show again to serve the next customer.

    
    


def make_coffee():
    choise = input(f"\nWhat would you like?:\n\
        Press 1 for Espresso\n\
        Press 2 for Latte\n\
        Press 3 for Cappuccino\n\
        Press Q to Quit\n\n")
    if choise == "off".lower():
        print('Goodbye!')
        sleep(1)
        quit()
    elif choise == "report".lower():
        print_report()
        make_coffee()
    elif choise not in MENU:
        print(f"\nSorry, wrong item.\n")
        make_coffee()
    else:
        print(f"Continue coding")


clear()
print("Welcome to our cofee machine programm!\n")
make_coffee()