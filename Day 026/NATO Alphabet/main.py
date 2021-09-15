# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
import pandas

data = pandas.read_csv("Day 026\\NATO Alphabet\\nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
nato_list = {row.letter:row.code for (index,row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word : ").upper()
output_list = [nato_list[letter] for letter in user_input]
print(output_list)
