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
    most_powerful = most_powerful.iloc[0]  # printing the first row of the most powerful car
    return most_powerful

# TODO: FIX THIS
# def find_most_powerful_car_by_mpg():
#     best_mpg = data.mpg.max()  # printing the most powerful car by mpg
#     best_hp = data.horsepower.max()  # printing the most powerful car by hp
#     final = data.iloc[data.mpg == best_mpg and data.horsepower == best_hp]  # printing the most powerful car by mpg
#     print(final)
#     return final
# find_most_powerful_car_by_mpg()
