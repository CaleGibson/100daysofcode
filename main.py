from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
end = False
while not end:
    coffee = menu.get_items()
    answer = input(f"What would you like to drink? {coffee}:")
    if answer == "off":
        end = True
    elif answer == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(answer)
        if coffee_maker.is_resource_sufficient(drink) and  money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)