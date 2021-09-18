import pandas

data = pandas.read_csv("Day 026\\NATO Alphabet\\nato_phonetic_alphabet.csv")

nato_list = {row.letter:row.code for (index,row) in data.iterrows()}

def generate_phonetics():
    user_input = input("Enter a word : ").upper()
    try:
        output_list = [nato_list[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetics()
    else:
        print(output_list)

generate_phonetics()