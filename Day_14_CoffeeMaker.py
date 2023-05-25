MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

def coffee_choice():
    return input("What would you like? (espresso/latte/cappuccino): ")
end = False
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
def resource_check(order_resources):
    for item in order_resources:
        if order_resources[item] > resources[item]:
            print(f"Sorry we dont have enough {item}")
            return False
    return True
def coin_counter():
    print("insert coins")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickels?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

def price_check(money_given, cost):
    if money_given >= cost:
        change = round( money_given - cost, 2)
        print(f"Your change is ${change}")
        global money
        money += cost
        return True
    else:
        print("Sorry not enough")
        return False

def make_coff(choice, order_ing):
    for item in resources:
        resources[item] -= order_ing[item]
    print(f"Here is your {choice}")
while not end:
    while not end:
        coffee = coffee_choice()
        if coffee == "report":
            print(f"{resources['water']}ml of water, {resources['milk']}ml of milk, {resources['coffee']}g of coffee, and ${money}")
        elif coffee == "off":
            end = True
        else:
            coff = MENU[coffee]
            if resource_check(coff["ingredients"]):
                total = coin_counter()
                if price_check(total, coff["cost"]):
                    make_coff(coffee, coff["ingredients"])
