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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def resource_report():
    print(f"The current amount of water is {resources['water']}, "
          f"the current amount of milk is {resources['milk']} "
          f"the current amount of coffee is {resources['coffee']}"
          f"and the current amount of money is {resources['money']}")



def get_payment(coffee_type):
    print(f"Please enter your payment {MENU[coffee_type]['cost']} in quarters/dimes/nickels and pennies")
    payment = int(input(f"How many quarters? ")) * .25
    payment += int(input(f"How many dimes? ")) * .10
    payment += int(input(f"How many nickels? ")) * .05
    payment += int(input(f"How many pennies? ")) * .01
    return payment


def payment_total(payment, cost):
    resources["money"] += cost
    return round(payment - cost, 2)


def check_resources():
    return


def update_resources():
    return


def coffee_machine():
    coffee_type = ""
    while coffee_type != 'off':
        coffee_type = input("What would you like? (espresso/latte/cappuccino):\n")
        if coffee_type == 'report':
            resource_report()
        else:
            drink_cost = MENU[coffee_type]['cost']
            print(f"The cost of {coffee_type} is {MENU[coffee_type]['cost']}")

            payment = round(get_payment(coffee_type), 2)
            print(payment)

            if payment >= drink_cost:
                change = payment_total(payment, drink_cost)
                print(f"Here is your {coffee_type}, enjoy your coffee")
                print(f"Here is your change {change} ")
            else:
                print("Not enough money BROKEY!!! GET A JOB!!")


coffee_machine()
