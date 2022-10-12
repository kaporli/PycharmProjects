from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random

RAND_H = random.randint(0, 360)

screen = Screen()

screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

score = Scoreboard()
game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 380:
        score.over_l()
    if ball.xcor() < -380:
        score.over_r()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

screen.exitonclick()