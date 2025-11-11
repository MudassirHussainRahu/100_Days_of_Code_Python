from turtle import Turtle
from random import randint

LEFT_LIMIT = -390
RIGHT_LIMIT = 390

COLORS = ["red", "white", "blue", "green", "orange", "purple", "black"]

class Car(Turtle):
    def __init__(self, y_axis):
        super().__init__("square")
        self.shapesize(stretch_len=0.5, stretch_wid= 4)
        self.penup()
        self.color(COLORS[randint(0,len(COLORS)-1)])
        self.shapesize(2,2)
        self.goto(RIGHT_LIMIT, y_axis)

    def move(self):
        (x,y) = self.position()
        self.goto(x-10, y)

