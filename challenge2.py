alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(t, s):
    for letter in range (0, len(t)):
        text_list = list(t)
        alph_index = alphabet.index(t[letter]) + s
        text_list[letter] = alphabet[alph_index]
        t = ''.join(text_list)
    print(f"The encoded text is {t}")

def decode(ct, sa):
    for letter in range (0, len(ct)):
        text_list = list(ct)
        alph_index = alphabet.index(ct[letter]) - sa
        text_list[letter] = alphabet[alph_index]
        ct = ''.join(text_list)
    print(f"The decoded text is {ct}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(t = text, s = shift)
elif direction == "decode":
    decode(ct = text, sa = shift)
else: 
    print(f"{direction} is not an option. Choose again.")