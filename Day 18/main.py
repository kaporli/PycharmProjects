import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.color("LightYellow4")

# tim.pensize(30)
tim.hideturtle()
tim.speed("fastest")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
degrees = [0, 90, 180, 270]
screen.colormode(255)

for i in range(80):
    tim.circle(150)
    tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.right(5)
    # tim.seth(random.choice(degrees))

screen = Screen()
screen.exitonclick()