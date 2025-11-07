from turtle import Turtle

UPPER_LIMIT = 280
LOWER_LIMIT = -280

LEFT_LIMIT = -380
RIGHT_LIMIT = 380

class Player(Turtle):
    player_count = 0
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        Player.player_count += 1
        
        if Player.player_count == 1:
            self.goto(LEFT_LIMIT,0)
        elif Player.player_count == 2:
            self.goto(RIGHT_LIMIT,0)
    
    def up(self):
        (x,y) = self.position()
        if y < UPPER_LIMIT:
            self.goto(x,y+20)

    def down(self):
        (x,y) = self.position()
        if y > LOWER_LIMIT:
            self.goto(x,y-20)
    
