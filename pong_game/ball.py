from turtle import Turtle
import random

BALL_COLOR = "white"
BALL_START_SPEED = 10
START_POSITION = (0, 0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOR)
        self.penup()
        self.shapesize(0.8)
        self.ball_speed = BALL_START_SPEED
        self.left_scored = random.randint(0, 1)
        self.refresh()

    def refresh(self):
        """Refresh ball position and future direction"""
        self.home()
        self.ball_speed = BALL_START_SPEED
        self.seth(random.randint(130, 230)) if self.left_scored else self.seth(random.randint(-50, 50))

    def move(self):
        """Ball moving sequence"""
        self.forward(self.ball_speed)
        self.check_bounce()
        return self.check_wall_collision()

    def check_wall_collision(self):
        """Return -1 if scored PC, 1 if scored User, 0 otherwise"""
        if self.xcor() < -500:
            self.left_scored = False
            self.refresh()
            return -1
        elif self.xcor() > 500:
            self.left_scored = True
            self.refresh()
            return 1
        return 0

    def check_bounce(self):
        """Wall bouncing"""
        if self.ycor() > 280 or self.ycor() < -280:
            self.seth(360 - self.heading())

    def platform_bounce(self):
        """Platform bouncing"""
        self.ball_speed += 2
        if 270 > self.heading() >= 180:
            self.seth(540 - self.heading())
        elif 180 > self.heading() > 90:
            self.seth(180 - self.heading())
        elif 90 > self.heading() >= 0:
            self.seth(180 - self.heading())
        elif 360 > self.heading() > 270:
            self.seth(180 - self.heading())
