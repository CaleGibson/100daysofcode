from turtle import Turtle, Screen
SCORE = 0
class Screen_set(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(10, -290)
        self.pensize(2)
        for _ in range(20):
            self.setheading(0)
            self.pendown()
            self.forward(10)
            self.setheading(90)
            self.forward(30)
            self.setheading(180)
            self.forward(10)
            self.setheading(270)
            self.forward(30)
            self.setheading(90)
            self.penup()
            self.forward(50)
    def scoreboard(self, x):
        self.score = SCORE
        self.goto(x, 230)
        self.write(f"{self.score}", font=('Consolas', 40, 'bold'))
    def add(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", font=('Consolas', 40, 'bold'))


