#!/usr/bin/env python3

# Aleksandr Verevkin
# Interactive coffee machine

from replit import clear
from data import MENU, resources


def report(coins):
    """Print out machine resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${coins}")


def input_handling(str, coins):
    """Switch trough user input.
       Return earned money"""
    match str:
        case 'espresso' | 'latte' | 'cappuccino':
            if not check_resources(str):
                return 0
            inserted = insert_coins()
            if not check_price(MENU[str]["cost"], inserted):
                return 0
            make_coffee(str)
            return MENU[str]["cost"]
        case 'off':
            print("Turning off...")
            exit(0)
        case 'report':
            report(coins)
            return 0
        case _:
            print("Wrong input")
            return 0


def make_coffee(coffee):
    """Remove resources from coffee machine and give coffee"""
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee]["ingredients"]["milk"] if coffee != "espresso" else 0
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    print(f"Here is your {coffee}. Enjoy!")


def insert_coins():
    """Return total amount of inserted coins"""
    print("Please insert coins.")
    inserted = int(input("How many quarters?: ")) * 0.25
    inserted += int(input("How many dimes?: ")) * 0.1
    inserted += int(input("How many nickles?: ")) * 0.05
    inserted += int(input("How many pennies?: ")) * 0.01
    return inserted


def check_price(price, inserted):
    """Return True if inserted coins were enough else False"""
    if price > inserted:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${inserted - price:.2f} in change.")
        return True


def check_resources(coffee):
    """Return True if machine have enough resources for chosen coffee else False"""
    if resources["water"] < MENU[coffee]["ingredients"]["water"] or \
        (resources["milk"] < MENU[coffee]["ingredients"]["milk"] if coffee != "espresso" else False) or \
            resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
        print("Sorry, not enough resources.")
        return False
    return True


if __name__ == "__main__":
    coins = 0
    while True:
        coins += input_handling(input("What would you like? (espresso/latte/cappuccino): "), coins)
