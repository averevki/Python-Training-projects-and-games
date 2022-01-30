#!/usr/bin/env python3

# Aleksandr Verevkin
# The Snake Game Project
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
SPEED = 0.1


def screen_setup():
    """Game screen setup"""
    temp_screen = Screen()
    temp_screen.setup(width=600, height=600, startx=2200, starty=200)
    temp_screen.tracer(0)
    temp_screen.bgcolor("black")
    temp_screen.title("The Snake Game")
    return temp_screen


def difficulty_popup():
    """Difficulty selection window"""
    if screen.textinput(title="Difficulty selection", prompt="Choose difficulty(normal/hard): ").lower() == "hard":
        global SPEED
        SPEED = 0.05


if __name__ == "__main__":
    screen = screen_setup()

    snake = Snake(3)
    screen.update()
    difficulty_popup()

    screen.listen()
    screen.onkeypress(key="a", fun=snake.turn_left)
    screen.onkeypress(key="d", fun=snake.turn_right)
    screen.onkeypress(key="w", fun=snake.turn_up)
    screen.onkeypress(key="s", fun=snake.turn_down)

    scoreboard = Score()
    time.sleep(0.5)
    food = Food()
    while snake.game_state:
        snake.game_on()
        time.sleep(SPEED)
        screen.update()
        if snake.head.distance(food) < 15:
            scoreboard.increase_score()
            snake.add_seg()
            food.refresh()
        snake.check_game_over()
    scoreboard.game_over()

    screen.exitonclick()
