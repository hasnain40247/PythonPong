from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore=0
        self.rscore=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.goto(-200,330)
        self.write(f"{self.lscore}",font=("Arial", 42, "bold"))
        self.goto(200, 330)
        self.write(f"{self.rscore}", font=("Arial", 42, "bold"))

    def updateLeft(self):
        self.lscore+=1
        self.updateScore()

    def updateRight(self):
        self.rscore+=1
        self.updateScore()