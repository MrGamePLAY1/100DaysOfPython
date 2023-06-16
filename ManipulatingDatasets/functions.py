#   _____                 _   _
#  |  ___|   _ _ __   ___| |_(_) ___  _ __  ___
#  | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#  |  _|| |_| | | | | (__| |_| | (_) | | | \__ \
#  |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#

import pandas as pd

data = pd.read_csv('data.csv')


def get_average_europe(mpg):
    rounded = round(235.215 / mpg, 2)
    return rounded


def find_most_powerful_car(car_data):
    most_powerful = car_data  # printing the most powerful car by displacement
    most_powerful = most_powerful.sort_values(by='horsepower', ascending=False)
    most_powerful = most_powerful.iloc[0]  # printing the first row of the most powerful car
    return most_powerful


# TODO: FIX THIS
def find_most_powerful_car_by_mpg(cars):
    best_mpg = cars.sort_values(by='mpg', ascending=False)
    best_hp = best_mpg.sort_values(by='horsepower', ascending=False)
    # The best car with the highest mpg and highest horsepower
    # print(best_hp.iloc[0])
    return best_hp.iloc[0]

