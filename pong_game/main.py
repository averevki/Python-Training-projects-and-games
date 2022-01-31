#!/usr/bin/env python3

# Aleksandr Verevkin
# The Pong Game Project
from threading import Timer
from turtle import Screen
from platform import Platform
from ball import Ball
from scoreboard import Score
import time
SPEED = 0.05
USER_START = (-470, 0)
PC_START = (470, 0)


def screen_setup():
    """Game screen setup"""
    temp_screen = Screen()
    temp_screen.setup(width=1000, height=600, startx=2000, starty=200)
    temp_screen.tracer(0)
    temp_screen.bgcolor("black")
    temp_screen.title("The Pong Game")
    return temp_screen


def game_off():
    """Turn off game"""
    global game_on
    game_on = False


if __name__ == "__main__":
    screen = screen_setup()
    my_platform = Platform(USER_START)
    pc_platform = Platform(PC_START)
    score = Score()
    ball = Ball()

    # Button binds
    screen.listen()
    screen.onkey(key="w", fun=my_platform.going_up)
    screen.onkey(key="s", fun=my_platform.going_down)
    screen.onkey(key="Up", fun=pc_platform.going_up)
    screen.onkey(key="Down", fun=pc_platform.going_down)
    screen.onkey(key="Escape", fun=game_off)

    # Game
    game_on = True
    while game_on:
        screen.update()

        result = ball.move()
        if result == 1:
            score.increase_left_score()
        elif result == -1:
            score.increase_right_score()

        if (my_platform.distance(ball) < 60 or pc_platform.distance(ball) < 60) and abs(ball.xcor()) > 440:
            ball.platform_bounce()

        time.sleep(SPEED)

    screen.exitonclick()
