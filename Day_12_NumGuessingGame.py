import random

EASY_LIVES = 10
HARD_LIVES = 5


def num_check(answer, guess, lives):
    if guess > answer:
        print("Too high")
        return lives - 1
    elif guess < answer:
        print("Too low")
        return lives - 1
    else:
        print(f"Correct the number is {answer}")


def diffuculty():
    version = input("Do you want the 'hard' or the 'easy' version? ")
    if version == "easy":
        return EASY_LIVES
    else:
        return HARD_LIVES


def game():
    print("Welcome the the guessing game. Im thinking of a number between 1 and 100")
    lives = diffuculty()

    answer = random.randint(1, 100)
    guess = 0
    while guess != answer:
        print(f"You have {lives} guesses")
        guess = int(input("Guess a number: "))
        lives = num_check(answer, guess, lives)
        if lives == 0:
            print("You lose")
            return


game()