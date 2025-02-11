# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("Input/Names/invited_names.txt") as file:
    # Read the entire content and split it into lines
    names = file.read().splitlines()


# with open("Input/Letters/starting_letter.docx") as file:
#     letter = file.readlines()
for name in names:
    with open(f"Output/ReadyToSend/Letter for {name}.txt", mode="w") as file:
        file.write(f"Dear {name},\nYou are invited to my birthday this Saturday.\nHope you can make it!\nAngela")
