alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def decrypt(plain_text):
    for shift_value in range(1,26):
        decrypted_word =""
        for letter in plain_text:
            if letter in alphabet :
                position = alphabet.index(letter)
                letter = alphabet[position-shift_value]
                decrypted_word +=letter    
            else:
                decrypted_word+=letter

        print(f"Your Decoded message is: {decrypted_word}")

user="yes"
while(user == "yes"):
    text = input("Type your message:\n").lower()
    decrypt(text)

    user=input("Do you want to Restart the Cipher Caesar Program? (yes/no)\n").lower()