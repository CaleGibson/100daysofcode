from Day_22_Ball import Ball
from Day_22_Paddles import Paddle
from turtle import Screen
from Day_22_screensetup import Screen_set
import time
game = True

screen1 = Screen()
screen1.setup(1200, 600)
screen1.bgcolor("black")
screen1.title("Pong")
screen1.tracer(0)
screen1.listen()
screen = Screen_set()
score1 = Screen_set()
score2 = Screen_set()
score1.scoreboard(-50)
score2.scoreboard(50)
ball = Ball()
paddle1 = Paddle()
paddle1.goto(-580, 0)
paddle2 = Paddle()
paddle2.goto(580, 0)
screen1.onkeypress(paddle2.up, "Up")
screen1.onkeypress(paddle2.down, "Down")
screen1.onkeypress(paddle1.up, "w")
screen1.onkeypress(paddle1.down, "s")
while game:

    screen1.update()
    if ball.xcor() > 590:
        score1.add()
        ball.rese(-570, 0, 1)
    if ball.xcor() < -590:
        score2.add()
        ball.rese(570, 0, 2)
    if ball.distance(paddle1) < 40:
        ball.reflect(1)
    if ball.distance(paddle2) < 40:
        ball.reflect(2)
    ball.move()
    ball.border()
    time.sleep(.002)



screen1.exitonclick()