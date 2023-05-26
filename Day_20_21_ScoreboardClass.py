from turtle import Turtle, Screen
ALIGN = "center"
FONT = ('ariel', 12, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
            super().__init__()
            self.score = 0
            self.penup()
            self.goto(0, 270)
            self.color("white")
            self.update()
            self.hideturtle()
    def update(self):
        self.write(f"Score: {self.score}", align='center', font=('ariel', 12, 'normal'))
    def over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=('ariel', 12, 'normal'))
    def add(self):
        self.clear()
        self.score +=1
        self.update()
