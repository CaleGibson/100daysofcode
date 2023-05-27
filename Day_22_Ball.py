from turtle import Turtle
import random
MOVE = 1
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.setheading(random.randint(0, 360))
    def move(self):
        self.forward(MOVE)
    def border(self):
        if self.ycor() > 280 or self.ycor() < -280:
                self.setheading(360 - self.heading())

    def rese(self, x, y, z):
        self.goto(x, y)
        if z == 1:
            self.setheading(random.randint(315, 405))
        if z == 2:
            self.setheading(random.randint(135, 225))
    def reflect(self, x):
        if x == 1:
            self.setheading(random.randint(315, 405))
        if x == 2:
            self.setheading(random.randint(135, 225))