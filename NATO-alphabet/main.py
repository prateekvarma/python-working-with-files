import pandas

# Program takes a word, and creates a list of NATO phonetic alphabets of it
# from a csv file

# TODO 1. Create a dictionary in this format:
data_df = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [data_dict[letter] for letter in word]
print(output_list)

