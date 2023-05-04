# Euro Coins: 1, 2, 5, 10, 20, 50, 1E, 2E
# Decimal Conversion: 0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00
from functions import *

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
print("Welcome to the Coffee Machine!")

user = input('What would you like? ')
if user.lower() == 'off':
    print('Coffee Machine is turning off.')
    exit()
else:
    print('\n That will be €', MENU[str(user)]['cost'], ' please. \n')

# TODO 2. Give change to the user
user_coin_input = float(input('Please insert coins: '))
change = user_coin_input - MENU[user]['cost']

if user_coin_input >= MENU[user]['cost']:
    print('Here is your change €', change)
else:
    print('Not enough money inserted. Please insert more coins.')

# TODO: 3. Once the user inputs what they want reduce the resources from the resources dictionary in functions.py


