import random 

#Make 2 art files 


#make a dictionary of 10 diffrent social media account with their followers
celebs = {"LeBron James": 163000000, "Tom Holland": 69000000, "Tom Cruise": 10000000, "Morgan Freeman": 4000000, "NFL": 29000000, "Zendaya":193000000, "Tom Brady": 15000000, "Leo Messi": 512000000,
"Cristiano Ronaldo": 643000000}
def celeb_select():
  celeb = random.choice(list(celebs))
  return celeb
def compare(cel1, cel2):
  if celebs.get(cel1) > celebs.get(cel2):
    winner = cel1
  else:
    winner = cel2
  return winner
def game():
  end = False
  score = 0
  A = celeb_select()
  B = celeb_select()
  while not end:
    while A == B:
      B = celeb_select()
    winner = compare(A, B)
    choice = input(f"Who has more followers? '{A}' or  '{B}': ")
    if choice == winner:
      score += 1

      print(f"Well done, your current score is {score}")
    else:
      print(f"You lose, your final score was {score}")
      end = True
    A = B
    B = celeb_select()
game()