from turtle import Turtle

FONT = ('Courier', 25, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 260)
        self.increase_score(0)

    def increase_score(self, add_score=1):
        """Score increasing"""
        self.clear()
        self.score += add_score
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        """Print game over sign"""
        self.home()
        self.write(arg="Game Over", align="center", font=FONT)
