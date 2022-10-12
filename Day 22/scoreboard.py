from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()

    def over_l(self):
        self.write(f"GAME OVER, PLAYER ONE SCORED", align=ALIGNMENT, font=FONT)
    def over_r(self):
        self.write(f"GAME OVER, PLAYER TWO SCORED", align=ALIGNMENT, font=FONT)
