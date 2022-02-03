#!/usr/bin/env python3

# Aleksandr Verevkin
# Password Manager Project with GUI using tkinter
import tkinter.messagebox
from tkinter import *
import pyperclip
import random
import json
START_EMAIL = "placeholder@gmail.com"
ENTRY_FILE = "data.json"  # file to save passwords


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Generate random password and copy it into clipboard
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = ''.join(password_list)
    inp_password.delete(0, 'end')
    inp_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    # Save password into .txt
    website = inp_website.get()
    email = inp_email.get()
    password = inp_password.get()
    new_data = {website: {"Email/Username": email, "Password": password}}

    if not website or not email or not password:
        tkinter.messagebox.showwarning(title="Empty field", message="Please don't leave any fields empty")
        return
    if tkinter.messagebox.askokcancel(title="Assertion", message=f"Entered details:\nWebsite: {website}\n"
                                                                 f"Email/Username: {email}\nPassword: {password}\n"
                                                                 f"Save?"):
        try:
            with open(ENTRY_FILE, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open(ENTRY_FILE, "w") as f:
                json.dump(new_data, f)
        else:
            data.update(new_data)
            with open(ENTRY_FILE, "w") as f:
                json.dump(data, f, indent=4)
        finally:
            tkinter.messagebox.showinfo(title="Success", message=f"Entry was saved into {ENTRY_FILE}")
            inp_password.delete(0, 'end')
            inp_website.delete(0, 'end')


# ---------------------------- SEARCH FOR EXISTING ------------------------------- #
def search():
    # Search for saved details
    website = inp_website.get()
    try:
        with open(ENTRY_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        tkinter.messagebox.showinfo(title="Website details", message="No data file found")
    else:
        if website in data:
            email = data[website]["Email/Username"]
            password = data[website]["Password"]
            tkinter.messagebox.showinfo(title="Website details", message=f"Details for {website}:\nEmail/Username: "
                                                                         f"{email}\n Password: {password}")
        else:
            tkinter.messagebox.showinfo(title="Website details", message=f"Details for {website} were not found")


# ---------------------------- UI SETUP ------------------------------- #
if __name__ == "__main__":
    # Main window
    window = Tk()
    window.config(padx=40, pady=40)
    window.title("Password Manager")
    # Logo
    canvas = Canvas(width=200, height=200, highlightthickness=0)
    lock_pic = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=lock_pic)
    canvas.grid(row=0, column=1, sticky="w")
    # Website label
    l_website = Label(text="Website:", highlightthickness=0)
    l_website.grid(column=0, row=1)
    # Email/Username label
    l_email = Label(text="Email/Username:", highlightthickness=0)
    l_email.grid(column=0, row=2)
    # Password label
    l_password = Label(text="Password:", highlightthickness=0)
    l_password.grid(column=0, row=3)
    # Website entry
    inp_website = Entry(width=21, justify='center')
    inp_website.grid(column=1, row=1, columnspan=2, sticky='w')
    inp_website.focus()
    # Email/Username entry
    inp_email = Entry(width=36, justify='center')
    inp_email.grid(column=1, row=2, columnspan=2, sticky='w')
    inp_email.insert(0, START_EMAIL)
    # Password entry
    inp_password = Entry(width=21)
    inp_password.grid(column=1, row=3, columnspan=2, sticky='w')
    # Generate Password button
    but_generate = Button(text="Generate Password", width=14, command=generate_password)
    but_generate.grid(column=1, row=3, columnspan=2, sticky='e')
    # Add button
    but_add = Button(text="Add", width=33, command=save_password)
    but_add.grid(column=1, row=4, columnspan=2, sticky='w')
    # Search button
    but_search = Button(text="Search", width=14, command=search)
    but_search.grid(column=1, row=1, columnspan=2, sticky='e')

    window.mainloop()
