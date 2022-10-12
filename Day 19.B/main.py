import turtle
from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(500,400)

colors = ["red", "green", "blue", "yellow", "pink"]
y_pos = [0, 20, -20, 40, -40]
turtles = []

for the_lads in range(0,5):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[the_lads])
    new_turtle.penup()
    new_turtle.goto(-200, y_pos[the_lads])
    new_turtle.speed(random.randint(10, 100))
    turtles.append(new_turtle)

user_bet = turtle.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False
            if user_bet == winning_turtle:
                print(f"You've won, the {winning_turtle} turtle won!")
            else:
                print(f"You've lost, the {winning_turtle} turtle won.")
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)


screen.exitonclick()
