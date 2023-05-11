# Euro Coins: 1, 2, 5, 10, 20, 50, 1E, 2E
# Decimal Conversion: 0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00, 2.00
from functions import *

print("Welcome to the Coffee Machine!")

user = input('What would you like? ')
lowered_user_input = user.lower()
print(lowered_user_input)

if lowered_user_input in MENU:
    user_selection(lowered_user_input)
    # dispense_coffee(lowered_user_input)
    repeat_program()

elif lowered_user_input == 'off':
    print('Coffee Machine is turning off.')
    exit()

# Printing the entire resources dictionary
elif lowered_user_input == 'report':
    print_report()
    repeat_program()

else:
    print('Invalid selection. Please try again. \n')
    # TESTING
    repeat_program()



