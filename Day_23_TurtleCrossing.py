import random
import time
from turtle import Screen
from Day_23_Player import Player
from Day_23_cars import CarManager
from Day_23_score import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car = CarManager()
tim = Player()
score = Scoreboard()

screen.listen()
screen.onkeypress(tim.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car1 in car.all:
        if car1.distance(tim) < 20:
            game_is_on = False
            score.end()

    sum = random.randint(1,10)
    if sum % 5 == 0:
        car.create()
    car.move()
    if tim.ycor() > 280:
        tim.next_lvl()
        score.add()
        car.lvl_up()

screen.exitonclick()