import random

def deal_card():
  """picks a random card"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card_delt = random.choice(cards)
  return card_delt


def calc_sum(cards):
  """takes cards and adds them together"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user, dealer):
  if user > 21 and dealer > 21:
    return"You lose went over"
  if user == dealer:
    return"Tie"
  elif user == 0:
    return"You win blackjack"
  elif dealer == 0:
    return"You lose dealer has blackjack"
  elif user > 21:
    return"went over you lose"
  elif dealer > 21: 
    return"dealer over you win"
  elif user > dealer:
    return"you win" 
  else:
    return("You lose")

def game():
  user_card = []
  dealer_card = []
  game_on = False
  for cards_chose in range (2):
    user_card.append(deal_card())
    dealer_card.append(deal_card())
  while not game_on:
    users_points = calc_sum(user_card)
    dealer_points = calc_sum(dealer_card)
    print(f"Your cards are {user_card} you have {users_points}")
    print(f"The dealers first cars is {dealer_card[0]} ")
    if dealer_points == 0 or users_points == 0:
      game_on = True
    else:
      cont_or_no = input("Would you like to another? 'y' or 'n' ")
      if cont_or_no == "y":
        user_card.append(deal_card())
      else:
        game_on = True
  while dealer_points > 0 and dealer_points < 17:
    dealer_card.append(deal_card())
    dealer_points = calc_sum(dealer_card)
  print(f"Your final hand is: {user_card} your final score is: {users_points}")
  print(f"The dealers hand is {dealer_card} their final score is:{dealer_points}")
  print(compare(users_points, dealer_points))
while input("Do you wnna play blackjack? 'y' or 'n' ") == 'y':
  game()
