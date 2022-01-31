from turtle import Turtle

FONT = ('Courier', 25, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt") as f:
                self.highest_score = int(f.read())
        except FileNotFoundError:
            with open("data.txt", "w") as f:
                f.write("0")
                self.highest_score = 0
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
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.write(arg=f"Score: {self.score} Highest Score: {self.highest_score}", align="center", font=FONT)

    def reset(self):
        """Reset game score"""
        with open("data.txt", "w") as f:
            f.write(str(self.highest_score))
        self.score = 0
        self.increase_score(0)
