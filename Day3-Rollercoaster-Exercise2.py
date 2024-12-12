# Using Logical Operators.
# Add an offer - Aged 45-55 gets free ticket due to midlife crisis.
print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm?"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $ 5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $ 7.")
    elif age >= 45 and age <= 55:
        print("You can have free ride")
    else:
        bill = 12
        print("Adult tickets are $ 12.")
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        # Add $ 3 to the ticket for photo taken.
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("You cannot ride the rollercoaster")