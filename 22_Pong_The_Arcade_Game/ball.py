from turtle import Turtle
from random import randint


HEADINGS = [0, 90, 180 ,270]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(1,1)
        self.x_move = 10
        self.y_move = 10
        self.reset()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        
    def reset(self):
        index = randint(0,3)
        self.setheading(HEADINGS[index])
        self.goto(0,0)

    