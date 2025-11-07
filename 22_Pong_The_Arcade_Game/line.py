from turtle import Turtle

UPPER_LIMIT = 290
LOWER_LIMIT = -290

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,LOWER_LIMIT)
        self.color("white")

        for i in range(int((UPPER_LIMIT-LOWER_LIMIT)/10)):
            if i%2 == 0:
                self.penup()
            else:
                self.pendown()
            (x,y) = self.position()
            self.goto(x,y+10)   