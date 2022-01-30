from turtle import Turtle
import random

FOOD_COLOR = "blue"


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(FOOD_COLOR)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Create new food piece"""
        self.setpos(random.randint(-280, 280), random.randint(-280, 280))

