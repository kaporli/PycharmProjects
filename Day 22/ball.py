from turtle import Turtle
import random

RAND_X = random.randint(-380, 380)
RAND_Y = random.randint(-280, 280)
RAND_H = random.randint(0, 360)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.7)
        self.pu()
        self.x_move = 3
        self.y_move = 3

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1




