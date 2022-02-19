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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def prompt_user():
    return input("What would you like? (espresso/latte/cappuccino): ")


def check_resources():
    ingredients = MENU[user_choice]["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry, not enough {ingredient}")
            return False
    return True


def print_price():
    print(f"The price of your {user_choice} is ${MENU[user_choice]['cost']}")


def deduct_resources():
    ingredients = MENU[user_choice]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


def print_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def make_payment():
    payment_types = {
        "quarter": 0.25,
        "dime": 0.1,
        "nickel": 0.05,
        "penny": 0.01,
    }
    payment = 0
    for payment_type in payment_types:
        user_input = int(input(f"How many {payment_type}s? "))
        payment += payment_types[payment_type] * int(user_input)
    change = payment - MENU[user_choice]["cost"]
    if change < 0:
        print("Sorry, not enough money")
        return False
    else:
        print(f"Your change is {change:.2f}")
        resources["money"] += MENU[user_choice]["cost"]
        return True


machine_on = True
while machine_on:
    user_choice = prompt_user()
    if user_choice in MENU:
        ingredients_avail = check_resources()
        if ingredients_avail:
            print_price()

    if user_choice == "espresso" and ingredients_avail:
        deduct_resources()
        if make_payment():
            print("Enjoy your espresso ☕!")
    elif user_choice == "latte" and ingredients_avail:
        deduct_resources()
        if make_payment():
            print("Enjoy your latte ☕!")
    elif user_choice == "cappuccino" and ingredients_avail:
        deduct_resources()
        if make_payment():
            print("Enjoy your cappuccino ☕!")
    elif user_choice == "report":
        print_resources()
    elif user_choice == "off":
        print("Machine is off")
        machine_on = False