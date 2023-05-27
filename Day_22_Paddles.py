from turtle import Turtle
START = [(0,20), (0, 0), (0, -20)]
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=8)


    def up(self):
        self.setheading(90)
        self.forward(10)

    def down(self):
        self.setheading(270)
        self.forward(10)

