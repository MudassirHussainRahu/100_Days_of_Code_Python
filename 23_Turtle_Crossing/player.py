from turtle import Turtle

MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
STARTING_POSITION = (0,-290)

class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.color("black")
        self.shapesize(1,1)
        self.setheading(90)
        self.penup()
        self.refresh()


    def refresh(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        (x,y) = self.position()
        self.goto(0, y+MOVE_DISTANCE)
    
    def move_down(self):
        (x,y) = self.position()
        self.goto(0, y-MOVE_DISTANCE)

    def finish_line(self):
        (x,y) = self.position()
        if y >= FINISH_LINE_Y:
            return True
        return False
    