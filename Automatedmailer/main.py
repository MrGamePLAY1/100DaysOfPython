# TODO: Create a letter using starting_letter.txt

names = open("Input/Names/invited_names.txt")
letter = open("Input/Letters/starting_letter.txt")
letter_contents = letter.read()

# for loop getting the names in invited_names.txt
for name in names:
    name = name.strip()  # gets the name stripped of the new line

    new_letter = letter_contents.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)
        completed_letter.close()
        print(f"Created {name}.txt")

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
