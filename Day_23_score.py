import random
from turtle import Turtle
FONT = ("Courier", 24, "normal")
SCORE = 1

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = SCORE
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.write(f"Level: {self.score}", font=FONT)


    def add(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", font=FONT)

    def end(self):
        self.goto(0, 0)
        self.write(f"Fat L, You Lose",align="center", font=FONT)