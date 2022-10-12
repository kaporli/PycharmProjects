from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.pu()
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def loop_back(self):
        self.goto(STARTING_POSITION)

    def is_at_finishline(self):
        if self.distance(0, FINISH_LINE_Y) < 20:
            return True
        else:
            return False

