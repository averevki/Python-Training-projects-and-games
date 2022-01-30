from turtle import Turtle

DEFAULT_SNAKE_PARTS = 3
SNAKE_COLOR = "white"
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self, start_snake_parts=DEFAULT_SNAKE_PARTS):
        self.snake = []
        self.snake_segments = start_snake_parts
        self.game_state = True
        self.start()
        self.head = self.snake[0]

    def start(self):
        """Snake initialization"""
        x = y = 0
        for num in range(self.snake_segments):
            turtle = Turtle(shape="square")
            turtle.penup()
            turtle.color(SNAKE_COLOR)
            turtle.goto(x, y)
            x -= MOVE_DISTANCE
            self.snake.append(turtle)

    def add_seg(self):
        """Add 1 snake element"""
        seg = Turtle(shape="square")
        seg.penup()
        seg.color(SNAKE_COLOR)
        seg.goto(self.snake[-1].pos())
        self.snake.append(seg)
        self.snake_segments += 1

    def turn_left(self):
        """Turn snake left"""
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def turn_right(self):
        """Turn snake right"""
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def turn_up(self):
        """Turn snake up"""
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def turn_down(self):
        """Turn snake down"""
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def game_on(self):
        """Start of the game"""
        for seg_num in range(self.snake_segments - 1, 0, -1):
            next_pos = self.snake[seg_num - 1].pos()
            self.snake[seg_num].setpos(next_pos)
        self.head.forward(MOVE_DISTANCE)

    def check_game_over(self):
        """Check for any collisions"""
        self.game_state = self.check_wall_collision() and self.check_seg_collision()

    def check_wall_collision(self):
        """Check for collision with wall"""
        return -280 < self.head.xcor() < 280 and -280 < self.head.ycor() < 280

    def check_seg_collision(self):
        """Check for collision with snake segment"""
        for seg in self.snake[1:]:
            if self.head.distance(seg) < 10:
                return False
        return True
