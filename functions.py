MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "black coffee": {
        "ingredients": {
            "water": 237,
            "milk": 0,
            "coffee": 1.33,
        },
        "cost": 1.5,
    },
    "flat white": {
        "ingredients": {
            "water": 200,
            "milk": 100,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "irish": {
        "ingredients": {
            "water": 200,
            "milk": 100,
            "coffee": 150,
            "sugar": 1,
            "cream": 2,
            "whiskey": 50,
        },
        "cost": 4.5,
    },
    "mocha": {
        "ingredients": {
            "water": 0,
            "milk": 250,
            "coffee": 18,
            "chocolate": 1,
        },
        "cost": 2.0,
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
    "water": 500,
    "milk": 500,
    "coffee": 500,
    "sugar": 500,
    "cream": 500,
    "whiskey": 500,
    "chocolate": 500,
}


def repeat_program():
    active = True
    while active:
        repeat = input('Invalid. Would you like to continue? (y/n) ')
        if repeat.lower() == 'y':
            selection = input('What would you like? ')
            lowered_selection = selection.lower()
            if lowered_selection in MENU:
                print('You have selected: ', lowered_selection)
                print('\n That will be €', MENU[str(lowered_selection)]['cost'], ' please. \n')
                user_coin_input = float(input('Please insert coins: '))
                dispense_coffee(lowered_selection)
                change = user_coin_input - MENU[lowered_selection]['cost']
                if user_coin_input >= MENU[lowered_selection]['cost']:
                    print('\n','Here is your change €', change)
                else:
                    print('Not enough money inserted. Please insert more coins.')
        else:
            active = False
            print('Thank you for using the Coffee Machine.')
            exit()


def dispense_coffee(userSelection):
    if userSelection.lower() == 'black coffee' or userSelection.lower() == 'black':
        print('\n \n Dispensing Black Coffee \n')

        print('Using 237ml of water')
        resources['water'] -= 237

        print('Using 1.33g of coffee')
        resources['coffee'] -= 1.33

    elif userSelection.lower() == 'latte':
        print('\n \n Dispensing Latte \n')

        print('Using 200ml of water')
        resources['water'] -= 200

        print('Using 150ml of milk')
        resources['milk'] -= 150

        print('Using 24g of coffee')
        resources['coffee'] -= 24

    elif userSelection.lower() == 'cappuccino':
        print('\n \n Dispensing Cappuccino \n')
        print('Using 250ml of water')
        resources['water'] -= 250

        print('Using 100ml of milk')
        resources['milk'] -= 100

        print('Using 24g of coffee')
        resources['coffee'] -= 24

    elif userSelection.lower() == 'flat white':
        print('\n \n Dispensing Flat White \n')
        print('Using 200ml of water')
        resources['water'] -= 200

        print('Using 100ml of milk')
        resources['milk'] -= 100

        print('Using 18g of coffee')
        resources['coffee'] -= 18

    elif userSelection.lower() == 'irish' or userSelection.lower() == 'irish coffee':
        print('\n \n Dispensing Irish Coffee \n')
        print('Using 200ml of water')
        resources['water'] -= 200

        print('Using 100ml of milk')
        resources['milk'] -= 100

        print('Using 150g of coffee')
        resources['coffee'] -= 150

        print('Using 1g of sugar')
        resources['sugar'] -= 1

        print('Using 2g of cream')
        resources['cream'] -= 2

        print('Using 50ml of whiskey')
        resources['whiskey'] -= 50

    elif userSelection.lower() == 'mocha':
        print('\n \n Dispensing Mocha \n')
        print('Using 250ml of milk')
        resources['milk'] -= 250

        print('Using 18g of coffee')
        resources['coffee'] -= 18

        print('Using 1g of chocolate')
        resources['chocolate'] -= 1
