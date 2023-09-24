alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(d, t, s):
    if s > 51:
        s = s % 52
        
    for letter in range (0, len(t)):
        text_list = list(t)
        if d == "encode" and t[letter] in alphabet:
            alph_index = alphabet.index(t[letter]) + s
            text_list[letter] = alphabet[alph_index]
        elif d == "decode" and t[letter] in alphabet:
            alph_index = alphabet.index(t[letter]) - s
            text_list[letter] = alphabet[alph_index]
        else:
            text_list[letter] = t[letter]
        t = ''.join(text_list)
    
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

    print(f"Here's the {d}d result: {t}") 

#TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
go_again = True
while go_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(d=direction, t=text, s=shift)
    restart = input("Do you want to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if restart == "yes":
        go_again = True 
    else:
        go_again = False 
        print("Goodbye!")


#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).