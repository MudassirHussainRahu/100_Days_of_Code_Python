from turtle import Turtle, Screen
import time
from running_cars import RunningCars
from player import Player
from random import randint
from scoreboard import ScoreBoard


LEFT_LIMIT = -390
RIGHT_LIMIT = 390
UPPER_LIMIT = 290
LOWER_LIMIT = -290


screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.tracer(0)



player = Player()
score = ScoreBoard()
cars = RunningCars()
screen.listen()

screen.onkey(key="w", fun=player.move_up)
screen.onkey(key="s", fun=player.move_down)


game_is_on = True

while game_is_on:
    if player.finish_line():
        player.refresh()
        score.increase_score()
        cars.level_up()


    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player)<20:
            game_is_on = False
            score.game_over()
    time.sleep(0.1)
    screen.update()
    

screen.exitonclick()