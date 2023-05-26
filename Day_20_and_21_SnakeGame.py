
from turtle import Screen
from Day_20_21_snakeClass import Snake
import time
from Day_20_21_snakefood import Food
from Day_20_21_ScoreboardClass import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = ScoreBoard()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

move = True
while move:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add()
        snake.add()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.over()
        move = False
    for segment in snake.segments[1:] :
        if snake.head.distance(segment) < 0.000001:
            move = False
            scoreboard.over()


screen.exitonclick()