from turtle import Turtle

FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-340, 260)
        self.level = 0
        self.write(f"LEVEL: {self.level}", font=FONT)

    def increase_score(self):
        self.clear()
        self.level += 1
        self.write(f"LEVEL: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!",align="center", font=FONT)