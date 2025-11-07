from turtle import Turtle

PLAYER_1_COORDINATES = (-100, 270)
PLAYER_2_COORDINATES = (100, 270)

FONT = ('Arial', 14, 'normal')


class ScoreBoard(Turtle):
    player_number = 0
    def __init__(self,):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        ScoreBoard.player_number += 1
        self.score = 0

        if ScoreBoard.player_number == 1:
            self.goto(PLAYER_1_COORDINATES)
        else:
            self.goto(PLAYER_2_COORDINATES)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"{self.score}", font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.refresh()