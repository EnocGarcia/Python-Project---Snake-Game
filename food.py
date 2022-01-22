from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("SkyBlue2")
        # self.shapesize(stretch_wid=.75, stretch_len=.75)
        self.speed("fastest")
        self.goto(x=randint(-280, 280), y=randint(-280, 255))

    def new_pos(self):
        self.goto(x=randint(-280, 280), y=randint(-280, 255))
