from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, font=('Arial', 50, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, font=('Arial', 50, 'normal'))

    def add_point_l(self):
        self.l_score += 1
        self.update_scoreboard()

    def add_point_r(self):
        self.r_score += 1
        self.update_scoreboard()