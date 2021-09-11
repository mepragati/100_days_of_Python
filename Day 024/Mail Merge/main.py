PLACEHOLDER = "[name]"

with open("Day 024\\Mail Merge\\Input\\Names\\invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Day 024\\Mail Merge\\Input\\Letters\\starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,strip_name) 
        with open(f"Day 024\Mail Merge\Output\ReadyToSend\letter_for_{strip_name}.txt","w") as completed_letter:
            completed_letter.write(new_letter)
