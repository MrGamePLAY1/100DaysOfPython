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


def dispense_coffee(userSelection):
    if userSelection.lower() == 'black coffee' or userSelection.lower() == 'black':
        print('\n \n Dispensing Black Coffee \n')

        print('Using 237ml of water')
        resources['water'] -= 237

        print('Using 1.33g of coffee')
        resources['coffee'] -= 1.33

        print('\n Cost: €1.50')
        print('Please insert coins')

    elif userSelection.lower() == 'latte':
        print('\n \n Dispensing Latte \n')

        print('Using 200ml of water')
        resources['water'] -= 200

        print('Using 150ml of milk')
        resources['milk'] -= 150

        print('Using 24g of coffee')
        resources['coffee'] -= 24

        print('\n Cost: €2.50')
        print('Please insert coins')

    elif userSelection.lower() == 'cappuccino':
        print('\n \n Dispensing Cappuccino \n')
        print('Using 250ml of water')
        resources['water'] -= 250

        print('Using 100ml of milk')
        resources['milk'] -= 100

        print('Using 24g of coffee')
        resources['coffee'] -= 24

        print('\n Cost: €3.00')
        print('Please insert coins')


    elif userSelection.lower() == 'flat white':
        print('\n \n Dispensing Flat White \n')
        print('Using 200ml of water')
        resources['water'] -= 200

        print('Using 100ml of milk')
        resources['milk'] -= 100

        print('Using 18g of coffee')
        resources['coffee'] -= 18

        print('\n Cost: €1.50')
        print('Please insert coins')

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

        print('\n Cost: €4.50')
        print('Please insert coins')

    elif userSelection.lower() == 'mocha':
        print('\n \n Dispensing Mocha \n')
        print('Using 250ml of milk')
        resources['milk'] -= 250

        print('Using 18g of coffee')
        resources['coffee'] -= 18

        print('Using 1g of chocolate')
        resources['chocolate'] -= 1

        print('\n Cost: €2.00')
        print('Please insert coins')
