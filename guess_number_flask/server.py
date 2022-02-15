#!/usr/bin/env python3

"""Guessing number game
Using flask server URL's
"""
__author__ = "Aleksandr Verevkin"
from flask import Flask
from random import randint
app = Flask(__name__)
win_num: int = randint(0, 9)


@app.route('/')
def start():
    """Start page, generate new random integer(0, 9)"""
    global win_num
    win_num = randint(0, 9)
    return '<h1 color="red">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:num>')
def guessing(num):
    """Handle all guessing pages"""
    global win_num
    if num > win_num:
        return '<h1 style="color:powderblue;">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif num < win_num:
        return '<h1 style="color:tomato;">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif num == win_num:
        return '<h1 style="color:green;">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
