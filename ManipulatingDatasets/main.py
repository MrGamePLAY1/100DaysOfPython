import pandas as pd
from functions import *

read_data = pd.read_csv("data.csv")
print(read_data)

average_mpg_all = read_data.mpg.mean()
average_mpg_all = round(average_mpg_all, 2)

print('\nAverage MPF for all cars: ', average_mpg_all)

#  Average MPG
average_usa_mpg = read_data.query('origin == "usa"')['mpg'].mean()
print('Average USA MPG: ', round(average_usa_mpg, 2))

average_europe_mpg = read_data.query('origin == "europe"')['mpg'].mean()
print('Average EUROPE MPG: ', round(average_europe_mpg, 2))

average_japan_mpg = read_data.query('origin == "japan"')['mpg'].mean()
print('Average JAPAN MPG: ', round(average_japan_mpg, 2))

# Converting mpg to KM/100km
average_km_all = get_average_europe(average_usa_mpg)
print('\nAverage MPG converted to KM/100km: ', average_km_all,'l')

average_km_europe = get_average_europe(average_europe_mpg)
print('Average mpg for Europe in KM/100km: ',average_km_europe,'l')
