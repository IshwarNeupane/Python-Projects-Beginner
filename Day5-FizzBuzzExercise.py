#Write a program that automatically generates the solution of FizzBuzz game.
total = 0
for number in range(1, 101):
    if number % 3 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
