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
    "bank balance": 0,
}


def addFundstoBank(coin, user_input):
    balance = 0

    # add coin input to balance
    balance += MENU[user_input]['cost']
    # Adding values to the bank balance
    resources['bank balance'] += balance

    balance_value = resources['bank balance']

    print('Bank Balance: €', balance_value)


def user_selection(user_input):
    print('You have selected: ', user_input)
    print('\n That will be €', MENU[user_input]['cost'], 'please. \n')

    # Taking coins
    coin_input = float(input('Please insert coins: '))

    # Checking inserted coins
    if coin_input >= MENU[user_input]['cost']:
        dispense_coffee(user_input)
        addFundstoBank(coin_input, user_input)

        # Change
        change = coin_input - MENU[user_input]['cost']
        print('\n Here is your change: €', change)
    else:
        print('Not enough inserted. Transaction cancelled')


def repeat_program():
    active = True
    while active:
        repeat = input('Would you like to continue? (y/n) ')

        if repeat.lower() == 'y':
            selection = input('What would you like? ')

            if selection == 'report':
                print_report()

            elif selection.lower() in MENU:
                user_selection(selection)
                dispense_coffee(selection)

            elif selection.lower() == 'n':
                active = False
                print('Thank you for using the Coffee Machine.')
                exit()

            # This function calculates user input, change and dispensing
            #


        else:
            print('Invalid input. Please try again.')


def print_report():
    print('\nWater:', resources['water'], 'ml',
          '\nMilk:', resources['milk'], 'ml',
          '\nCoffee:', resources['coffee'], 'g',
          '\nSugar:', resources['sugar'], 'g',
          '\nCream:', resources['cream'], 'ml',
          '\nWhiskey:', resources['whiskey'], 'ml',
          '\nChocolate:', resources['chocolate'], 'g', '\n'
          
          'Bank Balance: €', resources['bank balance'], '\n'
          )


def dispense_coffee(userSelection):
    if userSelection.lower() == 'black coffee' or userSelection.lower() == 'black':
        # if resources are 0 or less, print out of stock
        if resources['water'] >= 0 or resources['coffee'] >= 0:
            print('\n \n Dispensing Black Coffee \n')

            print('Using 237ml of water')
            resources['water'] -= 237

            print('Using 1.33g of coffee')
            resources['coffee'] -= 1.33

        elif resources['water'] <= 0 or resources['coffee'] <= 0:
            print('Out of stock')

    elif userSelection.lower() == 'latte':
        # if resources are 0 or less, print out of stock
        if resources['water'] >= 0 or resources['milk'] >= 0 or resources['coffee'] >= 0:
            print('\n \n Dispensing Latte \n')

            print('Using 200ml of water')
            resources['water'] -= 200

            print('Using 150ml of milk')
            resources['milk'] -= 150

            print('Using 24g of coffee')
            resources['coffee'] -= 24

        elif resources['water'] <= 0 or resources['milk'] <= 0 or resources['coffee'] <= 0:
            print('Out of stock')

    elif userSelection.lower() == 'cappuccino':
        # if resources are 0 or less, print out of stock
        if resources['water'] >= 0 or resources['milk'] >= 0 or resources['coffee'] >= 0:
            print('\n \n Dispensing Cappuccino \n')
            print('Using 250ml of water')
            resources['water'] -= 250

            print('Using 100ml of milk')
            resources['milk'] -= 100

            print('Using 24g of coffee')
            resources['coffee'] -= 24

        elif resources['water'] <= 0 or resources['milk'] <= 0 or resources['coffee'] <= 0:
            print('Out of stock')

    elif userSelection.lower() == 'flat white':
        # if resources are 0 or less, print out of stock
        if resources['water'] >= 0 or resources['milk'] >= 0 or resources['coffee'] >= 0:
            print('\n \n Dispensing Flat White \n')
            print('Using 200ml of water')
            resources['water'] -= 200

            print('Using 100ml of milk')
            resources['milk'] -= 100

            print('Using 18g of coffee')
            resources['coffee'] -= 18

        elif resources['water'] <= 0 or resources['milk'] <= 0 or resources['coffee'] <= 0:
            print('Out of stock')

    elif userSelection.lower() == 'irish' or userSelection.lower() == 'irish coffee':
        # if resources are 0 or less, print out of stock
        if resources['water'] >= 0 or resources['milk'] >= 0 or resources['coffee'] >= 0 or resources[
            'sugar'] >= 0 or resources['cream'] >= 0 or resources['whiskey'] >= 0:
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

        elif resources['water'] <= 0 or resources['milk'] <= 0 or resources['coffee'] <= 0 or resources[
            'sugar'] <= 0 or resources['cream'] <= 0 or resources['whiskey'] <= 0:
            print('Out of stock')

    elif userSelection.lower() == 'mocha':
        # if resources are 0 or less, print out of stock
        if resources['water'] >= 0 or resources['milk'] >= 0 or resources['coffee'] >= 0 or resources[
            'chocolate'] >= 0:
            print('\n \n Dispensing Mocha \n')
            print('Using 250ml of milk')
            resources['milk'] -= 250

            print('Using 18g of coffee')
            resources['coffee'] -= 18

            print('Using 1g of chocolate')
            resources['chocolate'] -= 1

        elif resources['water'] <= 0 or resources['milk'] <= 0 or resources['coffee'] <= 0 or resources[
            'chocolate'] <= 0:
            print('Out of stock')
