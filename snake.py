from turtle import Turtle
STEP = 20
DOT_LENGTH = 20
INITIAL_SIZE = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Dot(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(INITIAL_SIZE):
            dot = Dot()
            dot.goto(x=(-i * DOT_LENGTH), y=0)
            self.snake.append(dot)

    def add_tail(self):
        tail_idx = len(self.snake) - 1
        tail = self.snake[tail_idx]
        dot = Dot()
        dot.goto(tail.pos())
        self.snake.append(dot)

    def move(self):
        tail_idx = len(self.snake) - 1
        for i in range(tail_idx, 0, -1):
            dot = self.snake[i]
            prev_dot = self.snake[i - 1]
            dot.goto(prev_dot.pos())

        self.head.forward(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

# for _ in range(50):
#     sleep(.1)
#     screen.update()
#     head = snake[0]
#     # head.forward(20)
#     for i in range(len(snake)):
#         """a better way to implement this, instead of storing in memory the position of the old block
#         it's better to move from the tail to the head to the position of the segment -1"""
#         dot = snake[i]
#         bk_pos = dot.pos()
#         if i == 0:
#             dot.forward(20)
#         else:
#             dot.goto(fd_pos)
#         fd_pos = bk_pos
#
#     # if _ % 3 == 0:  # test
#     #     head.left(90)
