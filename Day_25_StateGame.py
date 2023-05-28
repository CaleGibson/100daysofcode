import turtle
import pandas
from Turt_class import State
data = pandas.read_csv("50_states.csv")
state_list = data["state"].tolist()

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess = []
misses = []
forever = True
stateNum = 0
while forever:
    answer_state = screen.textinput(title="Guess the State", prompt="What is a states name?" )
    for state in state_list:
        this_state = data[data.state == state]
        x_num = int(this_state.x)
        y_num = int(this_state.y)
        if answer_state == state:
            new = State()
            new.goto(x_num, y_num)
            new.write(state)
            stateNum += 1
            guess.append(answer_state)
    if stateNum >= 50 or answer_state == "stop":
        for all in state_list:
            if all not in guess:
                misses.append(all)
        print(f"You need to learn {misses}")
        forever = False



screen.exitonclick()
