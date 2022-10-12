from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.current_score = 0
        self.goto(0, 270)

    def over(self):
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1

    def score(self):
        self.write(f"Level: {self.current_score}", align=ALIGNMENT, font=FONT)
