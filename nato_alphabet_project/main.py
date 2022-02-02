#!/usr/bin/env python3

# Aleksandr Verevkin
# Nato Alphabet Project using dictionary comprehensions and pandas
import pandas

if __name__ == "__main__":
    alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
    alphabet_dict = {row.letter: row.code for index, row in alphabet.iterrows()}

    print([alphabet_dict[letter] for letter in input("Enter a word: ").upper()])
