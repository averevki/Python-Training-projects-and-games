#!/usr/bin/env python3

# Aleksandr Verevkin
# The Hirst Painting Project
from turtle import Turtle, Screen, colormode
import random
import colorgram

if __name__ == "__main__":
    colors = colorgram.extract('image.jpg', 30)[4:]

    tim = Turtle()
    tim.speed('fastest')
    colormode(255)
    tim.penup()
    tim.setpos(-250, -250)
    tim.pendown()
    next_pos = tim.pos()

    for _ in range(10):
        for _ in range(10):
            random_color = random.choice(colors)
            tim.dot(20, (random_color.rgb[0], random_color.rgb[1], random_color.rgb[2]))
            tim.penup()
            tim.forward(50)
            tim.pendown()
        tim.penup()
        next_pos = (next_pos[0], next_pos[1] + 50)
        tim.setpos(next_pos)
        tim.pendown()
    tim.hideturtle()


Screen().exitonclick()
