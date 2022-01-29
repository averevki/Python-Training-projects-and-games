from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cof_machine = CoffeeMaker()
mon_machine = MoneyMachine()
menu_items = Menu()

while True:
    inp = input(f"What would you like?({menu_items.get_items()}): ")
    if inp == "report":
        cof_machine.report()
        mon_machine.report()
    elif inp == "off":
        "Turning off..."
        exit(0)
    else:
        item = menu_items.find_drink(inp)
        if item is not None:
            if cof_machine.is_resource_sufficient(item) and mon_machine.make_payment(item.cost):
                cof_machine.make_coffee(item)

