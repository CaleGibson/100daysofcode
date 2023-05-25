rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = int(input("what do you choose? 0 = rock, 1 = paper,or 2 = scissors "))
RockPaperSissors = [rock, paper, scissors ]
import random
computers_choice = random.randint(0,2)
print(f"Computer chose:{RockPaperSissors[computers_choice]}")
print(f"you chose : {RockPaperSissors[choice]} ")
if choice == 0 and computers_choice == 2:
  print("you win")

if choice == 1 and computers_choice == 0:
  print("you win")

if choice == 2 and computers_choice == 1:
  print("you win")

if choice == computers_choice:
  print("you tie")
else: print("you lose")

