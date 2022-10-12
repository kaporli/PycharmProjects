from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    screen.update()
    car_manager.spawn_car()
    car_manager.move()

    scoreboard.score()
    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            scoreboard.over()
            game_is_on = False

    if player.is_at_finishline():
        player.loop_back()
        car_manager.speed_up()
        scoreboard.increase_score()
        scoreboard.clear()




screen.exitonclick()