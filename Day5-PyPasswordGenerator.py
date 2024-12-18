# Password generator program.
import random

letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "+",
    "&",
    "*",
]
print("Welcome to the Python Password Generator Program!")
nbr_letter = int(input("How many letters would you like in your password?\n"))
nbr_number = int(input("How many numbers would you like in your password?\n"))
nbr_symbol = int(input("How many symbols would you like in your password?\n"))
password_list = []
for char in range(1, nbr_letter + 1):
    password_list.append(random.choice(letters))
for char in range(1, nbr_number + 1):
    password_list += random.choice(numbers)
for char in range(1, nbr_symbol + 1):
    password_list += random.choice(symbols)
# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
