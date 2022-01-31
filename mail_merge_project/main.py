#!/usr/bin/env python3

# Aleksandr Verevkin
# Mail By Name Project
if __name__ == "__main__":
    with open("Input/Names/invited_names.txt") as names:
        names_list = names.readlines()
    with open("Input/Letters/starting_letter.txt") as example:
        example = example.read()
        for name in names_list:
            individual_mail = example.replace("[name]", name.strip())  # strip name out of new line sign
            print(individual_mail)
            with open(f"Output/ReadyToSend/{name}.txt", "w") as output:
                output.write(individual_mail)
