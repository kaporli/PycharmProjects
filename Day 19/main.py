from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def turn_right():
    tim.right(90)
def turn_left():
    tim.left(90)
def clear():
    tim.clear()

screen.listen()

screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_right)
screen.onkeypress(key="d", fun=turn_left)
screen.onkeypress(key="c", fun=clear)



screen.exitonclick()