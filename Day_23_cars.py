from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RAN_Y = random.randint(-230, 300)



class CarManager():
    def __init__(self):
        self.all = []


    def create(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.turtlesize(stretch_len=2)
        new_car.goto(300, random.randint(-230, 230))
        self.all.append(new_car)



    def move(self):
        for each in self.all:
            each.forward(STARTING_MOVE_DISTANCE)

    def lvl_up(self):
        current = STARTING_MOVE_DISTANCE
        up = MOVE_INCREMENT
        for each in self.all:
            each.forward(current + up)
