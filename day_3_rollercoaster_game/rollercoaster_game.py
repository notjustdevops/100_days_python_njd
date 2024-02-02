print("Welcome to RollerCoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride a RollerCoaster")
    age = int(input("What is you age?\n"))
    if age < 12:
        bill = 5
        print("Child Tikets are $5.")
    elif age <= 18:
        bill = 7
        print(" Youth Tickets are $7.")
    elif age >= 45 and age <= 55:
        print("You are in Mid Life crisis age. Don't worry, everything will be ok! Your have the Free Pass!") 
    else:
        bill = 12
        print("Adult Tickets are $12.")
    
    wants_photo = input("Do you wnat a photo taken? Y or N\n")
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your total bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.\n")