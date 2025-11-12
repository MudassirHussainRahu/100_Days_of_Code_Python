from turtle import Turtle

ALIIGNMENT = "center"
FONT = ("Courier", 20, "normal")



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,270)
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score:{self.score} HIGH SCORE:{self.high_score}", align=ALIIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def refresh(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=f"GAME OVER!", align=ALIIGNMENT, font=FONT)
