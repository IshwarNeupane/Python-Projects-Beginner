print("Welcome to the Caesar Cipher Program")
print("This program will encrypt and decrypt your message using the Caesar Cipher technique.")
print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Creating a function to encrypt and decrypt the message.
# The function will take the text, shift and direction as inputs.
def caesar(input_text, input_shift, input_direction):
    cipher_text = ""
    if input_direction == "decode":
        input_shift *= -1
#For characters, spaces and numbers that are not in the alphabet, the characters will be added to the cipher text as they are.
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + input_shift
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
   # for letter in input_text:
       # if letter in input_text:
           # position = alphabet.index(letter)
           # new_position = position + input_shift
           # new_letter = alphabet[new_position]
           # cipher_text += new_letter
       # else:
            # cipher_text += letter
    print(f"The {input_direction}d text is {cipher_text}")
# Each letter in the text will be shifted by the shift number and print the encrypted/decrypted message.
should_continue = True
while should_continue:    
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text=input("Type your message:\n").lower() 
    shift=int(input("Type the shift number:\n"))
    # If the shift number is greater than 25, the shift number will be reduced to the remainder of the shift number divided by 25.
    shift = shift % 25
    print(shift)
    caesar(input_text=text, input_shift=shift, input_direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("The Caesar Cipher program has ended.")
        print("Goodbye!")