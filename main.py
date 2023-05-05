# Euro Coins: 1, 2, 5, 10, 20, 50, 1E, 2E
# Decimal Conversion: 0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00
from functions import *

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
print("Welcome to the Coffee Machine!")

user = input('What would you like? ')
lowered_user_input = user.lower()
print(lowered_user_input)

if lowered_user_input == 'off':
    print('Coffee Machine is turning off.')
    exit()

# Printing the entire resources dictionary
elif lowered_user_input == 'report':
    print('\n Water: ', resources['water'], 'ml', '\n'
          'Milk: ', resources['milk'], 'ml','\n'
          'Coffee: ', resources['coffee'], 'g','\n'
          'Sugar: ', resources['sugar'], 'g','\n'
          'Cream: ', resources['cream'], 'ml','\n'
          'Whiskey: ', resources['whiskey'], 'ml','\n'
          'Chocolate: ', resources['chocolate'], 'g','\n')

# TODO: 2. Check if there are enough resources to be used in making the drink
# If there are enough resources then continue with the program
# If there are not enough resources then print “Sorry there is not enough water.”





# TODO 3. Give change to the user (Check if entered value is in the MENU)
# If found in the menu then continue with the program
if lowered_user_input in MENU:
    print('You have selected: ', lowered_user_input)
    print('\n That will be €', MENU[str(lowered_user_input)]['cost'], ' please. \n')
    user_coin_input = float(input('Please insert coins: '))
    dispense_coffee(lowered_user_input)
    change = user_coin_input - MENU[lowered_user_input]['cost']

else:
    print('Invalid selection. Please try again.')
    # TESTING
    repeat_program()

if user_coin_input >= MENU[user]['cost']:
    print('\n', 'Here is your change €', change)
else:
    print('Not enough money inserted. Please insert more coins.')






