from turtle import Turtle

FONT = ('Courier', 25, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-210, 250)
        self.level = 1
        self.level_refresh()

    def level_refresh(self):
        """Refresh level score"""
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT, align="center")

    def inc_level(self):
        """Increase level"""
        self.level += 1
        self.level_refresh()

    def game_over(self):
        """Print game over sign"""
        self.home()
        self.write(arg="GAME OVER", font=FONT, align="center")
