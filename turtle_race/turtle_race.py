#!/usr/bin/env python3

# Aleksandr Verevkin
# Turtle racing project
from turtle import Turtle, Screen
import random


def set_turt_pos(num, start_y):
    """Set turtles on start, return list with playing turtles"""
    turtles_list = []
    for num in range(num):
        turtles_list.append(Turtle(shape="turtle"))
        cur_turt = turtles_list[num]
        cur_turt.color(colors[num])
        cur_turt.penup()
        cur_turt.hideturtle()
        cur_turt.setpos(x=-230, y=start_y)
        start_y += 30
        cur_turt.showturtle()
        cur_turt.pendown()
    return turtles_list


def bet_popup(racers):
    """Return user bet as string"""
    prompt = "Choose between("
    prompt += "".join([colors[index] + "/" for index in range(racers)])
    prompt = prompt[:-1] + ")"
    return Screen().textinput(title="Bet on wining turtle", prompt=prompt).lower()


def start_race(racers):
    """Race process, return won index"""
    num = 0
    while True:
        index = num % racers
        turtles[index].forward(random.randint(0, 10))
        if turtles[index].pos()[0] >= 230:
            return index
        num += 1


def check_win(win_index, user_choice):
    """Check if user bet won"""
    if turtles[win_index].pencolor() == user_choice:
        print("You win, congratulations!")
    else:
        print("You lose")


def race_end(win_index):
    """Set wining screen"""
    for tur in turtles:
        if tur is not turtles[win_index]:
            tur.reset()
            tur.hideturtle()
        else:
            tur.home()
            tur.clear()

    turtles[win_index].write("WIN IS MINE!!!", font=("Arial", 12, "normal"), move=True)


if __name__ == '__main__':
    # Game setup
    colors = ["red", "blue", "yellow", "orange", "purple", "pink", "green", "black"]
    Screen().setup(width=500, height=400, startx=2200, starty=300)
    number_of_racers = 8

    # Game
    turtles = set_turt_pos(number_of_racers, -75)
    user_bet = bet_popup(number_of_racers)
    win_index = start_race(number_of_racers)
    check_win(win_index, user_bet)
    race_end(win_index)

    # Exit
    Screen().exitonclick()
