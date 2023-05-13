import menu
import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1: Prompt the user 'What would you like?'
user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO 2: Check the users input to check what to do next
# ------- All Objects -------
coffee = CoffeeMaker()  # Creating a CoffeeMaker Object
menu = Menu()  # Create a Menu Object
money = MoneyMachine()  # Creating a MoneyMachine Object

switch = True
items = menu.get_items()  # Making a list of all the items in the menu

while switch:
    if user_input == 'report'.lower():
        money_report = money.report()  # Creating a report of the money
        switch = False

    elif user_input == 'off'.lower():
        switch = False


    elif user_input in items:
        ingredients_forSelected = menu.find_drink(user_input)  # Finding the ingredients for the selected item
        cost_forSelected = ingredients_forSelected.cost  # Finding the cost for the selected item
        # report = coffee.report()  # Creating a report of the resources
        # Printing what the user selected
        print(f"You selected {user_input}.")

        # Printing the ingredients needed
        print("Ingredients needed: ", ingredients_forSelected.ingredients)

        # Printing the cost for selected
        print("Cost €: ", cost_forSelected)

        # Make payment
        money = money_machine.MoneyMachine()
        money_received = money.process_coins()
        print("€", money_received)

        # Check transaction successful
        if money_received >= cost_forSelected:
            # Dispensing Process
            coffee.make_coffee(ingredients_forSelected)
            print('Successful transaction')
            switch = False

        else:
            print('Transaction failed')
            switch = False

