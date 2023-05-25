from replit import clear
#HINT: You can call clear() to clear the output in the console.

name_bid = {}

def who_highest(biding_record):
  highest = 0
  winner = ""
  for bidder in biding_record:
    bid_ammount = int(biding_record[bidder])
                  #can get value^
    if bid_ammount > highest :
      highest = bid_ammount
      winner = bidder
  print(f"The winner is {winner} with {highest}")
end = False
while not end:  
    name = input("What is your name?")
    bid = input("How much would you like to bid? $")
    name_bid[name] = bid
    more = input("Are there any other bidders? Y or N ").lower()
    if  more =="n":
      end = True
      who_highest(name_bid)
    elif more =="y":
      clear()