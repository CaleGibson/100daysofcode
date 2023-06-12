from flask import Flask
import random
print(random.__name__)
print(__name__)
app = Flask(__name__)

def bold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper

@bold
@app.route('/')
def home():
    return '<h1>Guess a Number between 0 and 9</h1>' \
           '<img  src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

answer = random.randint(0,9)
@app.route("/<int:guess>")
def guess_number(guess):
    if guess > answer:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < answer:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)