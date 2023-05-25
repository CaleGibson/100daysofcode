print("Welcome to my tip calculator")
bill = int(input("What was the total bill?"))
tip_percent = int(input("what % would you like to tip?"))
ppl = input("How many people are paying?")
tip_decimal = tip_percent / 100
total = bill * (float(1) + tip_decimal)
per_person = round(float(total) / float(ppl),2) 
print("Each person should pay " + str(per_person))
