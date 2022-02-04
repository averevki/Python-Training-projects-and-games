#!/usr/bin/env python3

# Aleksandr Verevkin
# Flash Language Cards Project using tkinter
import pandas
import random
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
seen_words = []
current_card = None
timer = "after#0"  # None, string to avoid highlighting


def new_word():
    # Pick new card
    global timer
    global current_card
    window.after_cancel(timer)
    card_canvas.itemconfig(canvas_image, image=card_front_img)
    card_canvas.itemconfig(language_text, fill="black")
    card_canvas.itemconfig(word_text, fill="black")

    if len(data_list) == len(seen_words):
        card_canvas.itemconfig(language_text, text="")
        card_canvas.itemconfig(word_text, fill="red", text="All words are seen", font=(FONT_NAME, 40, "bold"))
        return

    current_card = random.choice(data_list)
    while current_card in seen_words:
        current_card = random.choice(data_list)

    seen_words.append(current_card)
    card_canvas.itemconfig(language_text, text="French")
    card_canvas.itemconfig(word_text, text=f"{current_card['French']}")
    timer = window.after(3000, flip_card)


def flip_card():
    # Flip current card
    card_canvas.itemconfig(canvas_image, image=card_back_img)
    card_canvas.itemconfig(language_text, text="English")
    card_canvas.itemconfig(word_text, text=f"{current_card['English']}")
    card_canvas.itemconfig(language_text, fill="white")
    card_canvas.itemconfig(word_text, fill="white")


def known_word():
    # Remove word from csv of unknown words and pick new card
    try:
        unknown_data = pandas.read_csv("data/words_to_learn.csv")
    except pandas.errors.EmptyDataError:
        return
    else:
        unknown_list = pandas.DataFrame.to_dict(unknown_data, orient="records")
        try:
            unknown_list.remove(current_card)
        except ValueError:
            return
        else:
            df = pandas.DataFrame(unknown_list)
            df.to_csv("data/words_to_learn.csv", index=False)
            new_word()


if __name__ == "__main__":
    # Read and save csv data into dictionary
    try:
        data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        data = pandas.read_csv("data/french_words.csv")
    except pandas.errors.EmptyDataError:
        data = pandas.read_csv("data/french_words.csv")
    data.to_csv("data/words_to_learn.csv", index=False)
    data_list = pandas.DataFrame.to_dict(data, orient="records")
    # Main window setup
    window = Tk()
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    window.title("Language cards")
    # Card setup
    card_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
    card_front_img = PhotoImage(file="images/card_front.png")
    card_back_img = PhotoImage(file="images/card_back.png")
    canvas_image = card_canvas.create_image(400, 263, image=card_front_img)
    language_text = card_canvas.create_text(400, 150, font=(FONT_NAME, 40, "italic"))
    word_text = card_canvas.create_text(400, 263, font=(FONT_NAME, 60, "bold"))
    card_canvas.grid(column=0, row=0, columnspan=2)
    # Red button
    no_img = PhotoImage(file='images/wrong.png')
    no_but = Button(highlightthickness=0, image=no_img, bg=BACKGROUND_COLOR, command=new_word)
    no_but.grid(column=0, row=1)
    # Green button
    yes_img = PhotoImage(file='images/right.png')
    yes_but = Button(highlightthickness=0, image=yes_img, bg=BACKGROUND_COLOR, command=known_word)
    yes_but.grid(column=1, row=1)

    new_word()
    window.mainloop()
