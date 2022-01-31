from turtle import Turtle


class Platform(Turtle):
    def __init__(self, start_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(start_position)

    def going_up(self):
        """Platform going up"""
        if self.ycor() < 280:
            self.setpos(self.xcor(), self.ycor() + 20)

    def going_down(self):
        """Platform going down"""
        if self.ycor() > -280:
            self.setpos(self.xcor(), self.ycor() - 20)

