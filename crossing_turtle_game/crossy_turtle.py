from turtle import Turtle

MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(stretch_wid=1.2, stretch_len=1.2)
        self.seth(90)
        self.reset_pos()

    def move(self):
        """Move turtle forward"""
        self.forward(MOVE_DISTANCE)

    def reset_pos(self):
        """Set player position on start"""
        self.goto(0, -280)
