with open("./Input/Names/invited_names.txt") as names:
    all_names = names.readlines()  # Reads each line and sets it as an item in list

with open("./Input/Letters/starting_letter.txt") as raw_letter:
    letter_content = raw_letter.read()  # Saves content of letter as string
    for name in all_names:
        stripped_name = name.strip()  # Strips off empty spaces including /n
        new_letter = letter_content.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}", mode="w") as completed_letter:
            completed_letter.write(new_letter)  # Writes string content into new file

