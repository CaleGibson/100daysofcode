def add(n1, n2):
  return n1 + n2
def sub(n1, n2):
  return n1 - n2
def multi(n1, n2):
  return n1 * n2
def div(n1, n2):
  return n1 / n2
operation = {
     "-":sub,
     "+":add,
     "*":multi,
     "/":div,
}

def calc():

  num1 = float(input("Whats the first number?: "))
  num2 = float(input("Whats the 2nd number?: "))
  oper = input("What operation do you want to   preform?'+', '-', '*', '/' : ")
  calc_funct = operation[oper]
  answer1 = calc_funct(num1, num2)
  print(f"{num1} {oper} {num2} = {answer1}")
  contin = True
  while contin:
    Y_or_N = input("Would you like to continue? 'y' or   'n' ")
    if Y_or_N == "n":
      contin = False
      calc()
    oper = input("Pick a new operation ")
    num3 = float(input("What is the next number? "))
    calc_funct = operation[oper]
    answer2 = calc_funct(answer1, num3)
    answer1 = answer2
    print(f"{answer1} {oper} {num3} = {answer2}")
calc()