# Write a program that works out whether if a given year is a leap year.
print("Welcome to find the Leap Year")
# Leap year evenly divisible by 4 except evenly divisible by 100 and unless evenly divisible by 400
Year = int(input("Enter the Year you want to check."))
if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("This is a leap year.")
        else:
            print("This is not a leap year.")
    else:
        print("This is not a leap year.")
else:
    print("This is not a leap year.")
