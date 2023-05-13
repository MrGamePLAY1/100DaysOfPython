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


def adding_money(money):
    bank = 0
    total = bank + money
    print('Total: €', total)


def user_selection(user_input):
    if user_input.lower() in MENU:
        print('You have selected: ', user_input)
        print('\n That will be €', MENU[user_input]['cost'], 'please. \n')

        # Taking coins
        coin_input = float(input('Please insert coins: '))

        # Checking inserted coins
        if coin_input >= MENU[user_input]['cost']:
            dispense_coffee(user_input)

            # Adding money to the bank
            adding_money(coin_input)

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

            # This function calculates user input, change and dispensing
            user_selection(selection)

        elif repeat.lower() == 'report':
            print_report()

        elif repeat.lower() == 'n':
            active = False
            print('Thank you for using the Coffee Machine.')
            exit()

        else:
            print('Invalid input. Please try again.')


def print_report():
    print('\nWater:', resources['water'], 'ml',
          '\nMilk:', resources['milk'], 'ml',
          '\nCoffee:', resources['coffee'], 'g',
          '\nSugar:', resources['sugar'], 'g',
          '\nCream:', resources['cream'], 'ml',
          '\nWhiskey:', resources['whiskey'], 'ml',
          '\nChocolate:', resources['chocolate'], 'g'
          )


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
