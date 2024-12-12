# Nested If else statement.
print("Welcome to the Nepal Zoo.")
Age = int(input("What is your age?"))
if Age <= 60:
    if Age <= 10:
        print("You can have free access in the zoo.")
    else:
        print("You have to pay NRs 200 for the zoo ticket.")
else:
    print("You have to pay NRs 50 for the zoo ticket.")
