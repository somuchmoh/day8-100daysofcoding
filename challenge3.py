alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

# def encrypt(t, s):
#     for letter in range (0, len(t)):
#         text_list = list(t)
#         alph_index = alphabet.index(t[letter]) + s
#         text_list[letter] = alphabet[alph_index]
#         t = ''.join(text_list)
#     print(f"The encoded text is {t}")

# def decode(ct, sa):
#     for letter in range (0, len(ct)):
#         text_list = list(ct)
#         alph_index = alphabet.index(ct[letter]) - sa
#         text_list[letter] = alphabet[alph_index]
#         ct = ''.join(text_list)
#     print(f"The decoded text is {ct}")

def caeser(d, t, s):
    for letter in range (0, len(t)):
        text_list = list(t)
        if d == "encode":
            alph_index = alphabet.index(t[letter]) + s
        else:
            alph_index = alphabet.index(t[letter]) - s
        text_list[letter] = alphabet[alph_index]
        t = ''.join(text_list)
    print(f"The {d}d text is {t}")
    



# if direction == "encode":
#     encrypt(t = text, s = shift)
# elif direction == "decode":
#     decode(ct = text, sa = shift)
# else: 
#     print(f"{direction} is not an option. Choose again.")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caeser(d=direction, t=text, s=shift)