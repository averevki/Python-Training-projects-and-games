#!/usr/bin/env python3

# Aleksandr Verevkin
# Mile to Km Converter Project using GUI by tkinter
from tkinter import *
FONT = ("Arial", 15)


def calculate_km():
    def wrapper():
        if not wrapper.used:
            wrapper.used = False  # True enable using this function only once
            l_res.config(text=round(int(inp.get()) * 1.6, 1))  # Miles->Km calculations
    wrapper.used = False
    return wrapper


if __name__ == "__main__":
    window = Tk()
    window.title("Mile to Km Converter")
    window.config(padx=20, pady=20)

    l_miles = Label(text="Miles", font=FONT)
    l_miles.grid(column=2, row=0)

    l_equal = Label(text="Is equal to", font=FONT)
    l_equal.grid(column=0, row=1)

    l_km = Label(text="Km", font=FONT)
    l_km.grid(column=2, row=1)

    l_res = Label(text="_", font=FONT)
    l_res.grid(column=1, row=1)

    button = Button(text="Calculate", command=calculate_km())
    button.grid(column=1, row=2)

    inp = Entry()
    inp.grid(column=1, row=0)

    window.mainloop()
