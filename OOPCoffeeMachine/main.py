import menu
import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 2: Check the users input to check what to do next
# ------- All Objects -------
coffee = CoffeeMaker()  # Creating a CoffeeMaker Object
menu = Menu()  # Create a Menu Object
money = MoneyMachine()  # Creating a MoneyMachine Object

switch = True

while switch:
    options = menu.get_items()
    selection = input(f'What you would like ({options}): ')

    if selection == 'report':
        coffee.report()
        money.report()

    elif selection == 'off':
        switch = False

    else:
        drink = menu.find_drink(selection)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)

