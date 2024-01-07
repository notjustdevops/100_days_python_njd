print("\nWelcome to the Tip calculator.\n")
total_bill = int(input("What was the total biil?\n"))
percentage_tip = int(input("\nWhat procentage tip would you like to gibe?\n10, 12, 15?\n"))
percentage_tip = float(percentage_tip / 100)
people_splitting_the_bill = int(input("\nHow many people are splitting this bill?\n"))
personal_bill_calculation = (total_bill + (total_bill * percentage_tip)) / people_splitting_the_bill

print(f"\nEach person should pay: {personal_bill_calculation} Euro\n")