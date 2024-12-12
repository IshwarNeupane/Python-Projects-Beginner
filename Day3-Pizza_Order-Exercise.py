# Pizza delivery Service
print("Welcome to Python Pizza Delivery Service")
size = input(
    "What size do you want(small, medium or large)?\n Press S for small, M for Medium and L for Large"
)
add_pepperoni = input(
    "Do you want to add pepperoni? Press 'Y' for Yes, Press 'N' for No"
)
extra_cheese = input("Do you want to extra cheese? Press 'Y' for Yes, Press 'N' for No")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
    
if add_pepperoni == "Y":
    # Add $2 for pepperoni in Small pizza.
    if size == "S":
        bill += 2
    else:
        # Add $3 for pepperoni in Medium and Large pizza.
        bill += 3
    if extra_cheese == "Y":
        # Add $1 for extra cheese.
        bill += 1
print(f"Your final bill is ${bill}")
