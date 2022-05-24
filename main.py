MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
#######################################################


def check_recourses(drink_choice):
    n_water = MENU[drink_choice]["ingredients"]["water"]
    n_milk = MENU[drink_choice]["ingredients"]["milk"]
    n_coffee = MENU[drink_choice]["ingredients"]["coffee"]
    if n_water > resources["water"]:
        print("Sorry, not enough water")
        return False
    if n_milk > resources["milk"]:
        print("Sorry, not enough milk")
        return False
    if n_coffee > resources["coffee"]:
        print("Sorry, not enough coffee")
        return False
    else:
        return True


def coins_operator():
    print("Please insert coins")
    quarters = int(input("Quarters ")) * 0.25
    dimes = int(input("Dimes ")) * 0.10
    nickles = int(input("Nickles ")) * 0.05
    pennies = int(input("Pennies ")) * 0.01
    return quarters + dimes + nickles + pennies


def transaction(user_money, cost):
    if user_money < cost:
        print("Sorry, not enough money. Money refunded")
        return False
    else:
        print(f"Here is your change: {round(user_money - cost, 2)} ")
        return True


def make_coffee(drink_choice):
    resources["water"] -= MENU[drink_choice]["ingredients"]["water"]
    resources["milk"] -= MENU[drink_choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink_choice]["ingredients"]["coffee"]
    resources["money"] += MENU[drink_choice]["cost"]
    print(f"Here is your {drink_choice}.Enjoy!")


def main_menu():
    drink_choice = input("What would you like? (espresso($1.5)/latte($2.5)/cappuccino($3.0): ")
    if drink_choice == "off":
        global turn_off
        turn_off = True
    elif drink_choice == "report":
        print(f"Resources left:\n{resources}")
    else:
        price = MENU[drink_choice]["cost"]
        print(f"{drink_choice} is {price}")
        if check_recourses(drink_choice):
            if transaction(coins_operator(), price):
                make_coffee(drink_choice)


turn_off = False
while not turn_off:
    main_menu()
