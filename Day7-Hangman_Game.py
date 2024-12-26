print("Welcome to Hangman Game.")
print(
    """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
"""
)

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]
import random
from hangman_words import word_list

# Delete this line. Used to check while coding only.  word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# Set lives in the game for user.
lives = 6
# Testing Code.
# print(f"The chosen word is: {chosen_word}")
# Step 1: Create an empty list called display for the random word selected.
# For each letter in the chosen word, add "_" to display.
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)
# Step 2: Loop through in the position of chosen_word.
# If the letter at the position matches the guess, replace the "_" with the letter.
# Print the display list.

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:").lower()
    # Check guessed letter.
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Sorry, You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("Congratulations, You win.")
    print(stages[lives])
