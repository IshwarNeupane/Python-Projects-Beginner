print("Welcome to the love calculator")
Your_name = input("What is your name?")
Partner_name = input("What is your partner's name?")
Combined_name = Your_name + Partner_name
lower_case_Combined_name = Combined_name.lower()
t = lower_case_Combined_name.count("t")
r = lower_case_Combined_name.count("r")
u = lower_case_Combined_name.count("u")
e = lower_case_Combined_name.count("e")
true = t + r + u + e
l = lower_case_Combined_name.count("l")
o = lower_case_Combined_name.count("o")
v = lower_case_Combined_name.count("v")
e = lower_case_Combined_name.count("e")
love = l + o + v + e
love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you go alright together.")
else:
    print(f"Your love score is {love_score}")
