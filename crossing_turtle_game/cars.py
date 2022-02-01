from turtle import Turtle
import random
COLORS = ["purple", "yellow", "orange", "blue", "green", "red"]
CARS_COUNT = 25
START_SPEED = 5
INC_SPEED = 3


class Cars:
    def __init__(self):
        self.car_list = []
        self.speed = START_SPEED
        for _ in range(CARS_COUNT):
            car = Turtle(shape="square")
            car.speed("fastest")
            car.color(random.choice(COLORS))
            car.penup()
            car.seth(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(random.randint(-350, 450), random.randint(-230, 250))
            self.car_list.append(car)

    def move(self):
        """Cars moving sequence"""
        for car in self.car_list:
            car.forward(self.speed)
            if car.xcor() < -450:
                car.goto(random.randint(350, 500), random.randint(-230, 250))

    def inc_speed(self):
        """Slightly increase cars speed"""
        self.speed += INC_SPEED
