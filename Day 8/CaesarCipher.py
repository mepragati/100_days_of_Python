import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

# def encrypt(plain_text,shift_value):
#   encrypted_word = ""
#   for letter in plain_text:
#         if letter == ' ':
#             encrypted_word+=letter
#         else:
#             position = alphabet.index(letter)
#             letter = alphabet[position+shift_value]
#             encrypted_word +=letter

#   print(f"Your Encoded message is: {encrypted_word}")  

# def decrypt(plain_text,shift_value):
#     decrypted_word =""
#     for letter in plain_text:
#         if letter == ' ':
#             decrypted_word+=letter
#         else:
#             position = alphabet.index(letter)
#             letter = alphabet[position-shift_value]
#             decrypted_word +=letter
    
#     print(f"Your Decoded message is: {decrypted_word}")

def caesar(plain_text,shift_value,new_direction):
  changed_text =""
  if new_direction == "decode":
      shift_value *= -1

  for letter in plain_text:
    if not letter.isalpha():
        changed_text+=letter
    else:
        position = alphabet.index(letter)
        changed_text += alphabet[position + shift_value]
  print(f"The {new_direction}d text is: {changed_text}")


print(logo.logo)
user="yes"
while(user == "yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if(direction!="encode" and direction!="decode"):
        print(logo.invalid)
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if(shift>26):
        shift=shift%26

    caesar(text,shift,direction)

    user=input("Do you want to Restart the Cipher Caesar Program? (yes/no)\n").lower()

# if(direction == "encode"):
#   encrypt(text,shift)
# elif(direction == "decode"):
#     decrypt(text,shift)
# else:
#     print("Invalid Choice!!")