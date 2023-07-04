import csv
import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = {}

# CSV
csv_data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dic = {row.letter: row.code for (index, row) in csv_data.iterrows()}
# print(phonetic_dic)

input_value = input("Enter a word: ").upper()

# try, except
try:
    output_list = [phonetic_dic[letter] for letter in input_value]
except KeyError:
    print('Sorry only letters in the alphabet please')
finally:
    print(output_list)
