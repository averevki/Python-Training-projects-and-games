#!/usr/bin/env python3

# Aleksandr Verevkin
# Crossy Road Game Project
from turtle import Screen
from crossy_turtle import Player
from scoreboard import Score
from cars import Cars
from time import sleep


def screen_setup():
    """Game screen setup"""
    temp_screen = Screen()
    temp_screen.setup(width=600, height=600, startx=2200, starty=200)
    temp_screen.tracer(0)
    temp_screen.title("Crossy Road Game")
    return temp_screen


if __name__ == "__main__":
    # Set up
    screen = screen_setup()
    score = Score()
    crossing = Player()
    cars = Cars()
    screen.update()

    screen.listen()
    screen.onkeypress(key="w", fun=crossing.move)
    screen.onkeypress(key="Up", fun=crossing.move)

    # Game
    game_on = True
    while game_on:
        cars.move()

        if crossing.ycor() > 270:
            score.inc_level()
            crossing.reset_pos()
            cars.inc_speed()

        for car in cars.car_list:
            if crossing.distance(car) < 25:
                score.game_over()
                game_on = False

        sleep(0.1)
        screen.update()

    screen.exitonclick()
