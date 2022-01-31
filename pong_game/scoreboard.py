from turtle import Turtle

FONT = ('Comic Sans', 50, "normal")


class Line(Turtle):
    def __init__(self):
        """Middle line drawing"""
        super().__init__()
        self.pencolor("white")
        self.pensize(5)
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, -280)
        self.left(90)
        for _ in range(29):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.line = Line()
        self.left_score = 0
        self.my_scored = True
        self.right_score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.refresh_score()

    def increase_left_score(self):
        """Increase left score"""
        self.my_scored = True
        self.left_score += 1
        self.refresh_score()

    def increase_right_score(self):
        """Increase right score"""
        self.my_scored = False
        self.right_score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.left_score}", font=FONT, align="center")
        self.goto(100, 200)
        self.write(f"{self.right_score}", font=FONT, align="center")
