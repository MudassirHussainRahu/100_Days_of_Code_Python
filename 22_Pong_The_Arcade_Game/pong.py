import time
from turtle import Turtle, Screen
from player import Player
from ball import Ball
from scoreboard import ScoreBoard
from line import Line


UPPER_LIMIT = 280
LOWER_LIMIT = -280

LEFT_LIMIT = -380
RIGHT_LIMIT = 380


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Arcade Game")
screen.tracer(0)
screen.listen()


line = Line()

score1 = ScoreBoard()
score2 = ScoreBoard()

player1 = Player()
player2 = Player()

ball = Ball()


screen.onkey(key="w", fun=player1.up)
screen.onkey(key="s", fun=player1.down)
screen.onkey(key="Up", fun=player2.up)
screen.onkey(key="Down", fun=player2.down)

game_is_on = True

while game_is_on:
    time.sleep(0.1)    
    screen.update()
    ball.move()

    if ball.ycor() > UPPER_LIMIT or ball.ycor() < LOWER_LIMIT:
        ball.bounce_y()
    
    if ball.distance(player1)<30 and ball.xcor()>LEFT_LIMIT or ball.distance(player2)<30 and ball.xcor()< RIGHT_LIMIT :
        ball.bounce_x()
    elif ball.distance(player1)>30 and ball.xcor()<LEFT_LIMIT or ball.distance(player2)>30 and ball.xcor()> RIGHT_LIMIT :
        if ball.xcor()>0:
            score1.increase_score()
        else:
            score2.increase_score()
        ball.reset()
    

    

    
    
    



screen.exitonclick()