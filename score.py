from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.play1_score = 0
        self.play2_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 300)
        self.write(self.play2_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 300)
        self.write(self.play1_score, align="center", font=("Courier", 80, "normal"))

    def r_score(self):
        self.play1_score += 1
        self.update()

    def l_score(self):
        self.play2_score += 1
        self.update()