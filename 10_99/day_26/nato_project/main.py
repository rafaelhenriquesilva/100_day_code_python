import pandas
from pathlib import Path
#TODO 1. Create a dictionary in this format:
file_path = Path(__file__).parent / "nato_phonetic_alphabet.csv" 
data = pandas.read_csv(file_path)
phonetic_dict = {row.letter: row.code for (_, row) in data.iterrows()}
#print(phonetic_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word_user = input('Enter a word: Test').upper()
output_list = [phonetic_dict[letter] for letter in word_user]
print(output_list)



