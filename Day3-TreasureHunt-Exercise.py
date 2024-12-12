print("Welcome to the treasure island")
print(
    """
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 """
)
print("Your mission is to find treasure")
print(
    '''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
'''
)
choice1 = input('You are at a crossroad, where you want to go? type "left" or "right".').lower()
if choice1 == "left":
   choice2= input('You have come to a river. Do you want to swim or wait for the boat? type "swim" or "boat".').lower()
   if choice2=="boat":
       choice3=input('You reached the island unharmed. There is a house with 3 doors- red, blue and green. Type "red" or "blue" or "green" to enter.').lower()
       if choice3=="red":
           print("There was a dragon inside. Game Over!")
       elif choice3=="blue":
           print("The room was full of snakes. Game Over!")
       elif choice3=="green":
           print("Congratulations, you found the treasure. You won!")
       else:
           print("You entered wrong option. You were killed by a demon. Game Over!")
   else:
       print("You have been attacked by a crocodile. Game Over!")
else:
   print("You went to the jungle and hunted by a tiger. Game Over!") 

