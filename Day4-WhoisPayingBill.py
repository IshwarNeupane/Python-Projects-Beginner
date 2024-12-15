# "Who is paying the bill" program
import random

test_seed = int(input("Enter a seed number:"))
random.seed(test_seed)

# split string method
namesAsCSV = input("Give me everybody names separated by a comma")
names = namesAsCSV.split(", ")
# Fetch total number of items from the list.
num_items = len(names)
# Generate random numbers between 0 and the last item index.
random_choice = random.randint(0, num_items - 1)
person_paying = names[random_choice]
print(f"{person_paying} is going to pay the meal today.")

#Alternatively, you can use choice function for the program too.
#Start from line 10 as follows:
#person_paying=random.choice(names)
#print(f"{person_paying} is going to pay the meal today."))
