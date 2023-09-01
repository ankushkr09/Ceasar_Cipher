#create a list of alphabets from a-z
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#define a function that will take three parameters as input(original_text, shift_amount_direction to encode or decode)
def caesar(cipher_direction,start_text, shift_amount):
    end_text = ''  #assign a empty string
    if cipher_direction == 'decode':   #to supress the code as make it less space consuming doing this
        shift_amount *= -1   #when we want to decode the word than we will have to go that much step back.

    for char in start_text:
        #if that character is available in alphabet list:
        if char in alphabet:
            #take out its position from alphabet list
            position = alphabet.index(char)  
            #now new position will be current position added top shift amount
            new_position = position + shift_amount
            #add those characters to end_text variable which are present at new position index of alphabet
            end_text += alphabet[new_position]
        else:   #if that character is not in alphabet list[]
            end_text += char  #add those char/symbol/space as it is to end_text variable:
    #print the encoded or decoded word
    print(f"Your {cipher_direction}d word is: '{end_text}'")

#from art module import logo
from art import logo
print(logo)

#assign a variable play_again to True(bool)
play_again = True
#till the condition of play_again will be true, it will keep going through while loop:
while play_again:
    #taking user's input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26 #if someone gives shift more than the index available at alphabet list

    #after taking the inputs call the function caesar
    caesar(cipher_direction=direction, start_text=text, shift_amount=shift)

    #ask again to user if they want to go again:
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    
    if result == 'no':  #if the result is no
        play_again = False   #change the play_again variable value to False from True, which will end the while loop as the while condition will become false
        print("Good Bye!")
