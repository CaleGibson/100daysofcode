import turtle
from turtle import Turtle, Screen
screen = Screen()
import random
is_race_on = False
screen.setup(width=500, height=400)
all_turtles = []


colors = ["red", "blue", "orange", "brown", "purple", "green"]
choice = 0
y = 100
for turtle_index in range(0, 6):
    New_Turtle = Turtle(shape="turtle")
    New_Turtle.color(colors[turtle_index])
    choice += 1
    New_Turtle.penup()
    New_Turtle.goto(-230, y)
    y -= 33
    all_turtles.append(New_Turtle)

user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"You win,the {turtle.pencolor()} turtle won!")
            else:
                print(f"You lose, the {turtle.pencolor()} turtle won!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()
