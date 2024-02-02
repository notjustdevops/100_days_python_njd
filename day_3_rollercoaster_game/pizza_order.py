print("\nThank you for choosing Python Pizza Deliveries!\nChoose pizza size: S, M or L:")
size = input() # What size pizza do you want? S, M, or L
print("\nChoose to Add Pepperoni (Y or N)")
add_pepperoni = input() # Do you want pepperoni? Y or N
print("\nAdd Extra Cheese just for $1! (Y or N)")
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

Small_pizza = 15
Medium_pizza = 20
Large_pizza = 25

Small_pizza_pepperoni = 2
Medium_or_large_pizza_pepperoni = 3
Extra_cheese_all_sizes = 1

bill = 0


if size == "L":
    bill += Large_pizza
    if add_pepperoni == "Y":
        bill += Medium_or_large_pizza_pepperoni
    if extra_cheese == "Y":
        bill += Extra_cheese_all_sizes

elif size == "M":
    bill += Medium_pizza
    if add_pepperoni == "Y":
        bill += Medium_or_large_pizza_pepperoni
    if extra_cheese == "Y":
        bill += Extra_cheese_all_sizes

elif size == "S":
    bill += Small_pizza
    if add_pepperoni == "Y":
        bill += Small_pizza_pepperoni
    if extra_cheese == "Y":
        bill += Extra_cheese_all_sizes
        
print(f"\nThank you for choosing Python Pizza Deliveries! Your final bill is: ${bill}\n")