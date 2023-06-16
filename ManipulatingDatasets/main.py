from functions import *

read_data = pd.read_csv("data.csv")
print(read_data)

average_mpg_all = read_data.mpg.mean()
average_mpg_all = round(average_mpg_all, 2)

print('\nAverage MPF for all cars: ', average_mpg_all)

#  Average MPG ----------------------------------------------------------------------
average_usa_mpg = read_data.query('origin == "usa"')['mpg'].mean()
print('\nAverage USA MPG: ', round(average_usa_mpg, 2))

average_europe_mpg = read_data.query('origin == "europe"')['mpg'].mean()
print('Average EUROPE MPG: ', round(average_europe_mpg, 2))

average_japan_mpg = read_data.query('origin == "japan"')['mpg'].mean()
print('Average JAPAN MPG: ', round(average_japan_mpg, 2))

# ----------------------------------------------------------------------------------

# Converting mpg to KM/100km ------------------------------------------------------
average_km_all = get_average_europe(average_usa_mpg)
print('\nAverage mpg converted to KM/100km: ', average_km_all, 'l')

average_km_europe = get_average_europe(average_europe_mpg)
print('Average mpg for Europe in KM/100km: ', average_km_europe, 'l')

average_km_japan = get_average_europe(average_japan_mpg)
print('Average mpg for Japan in KM/100km: ', average_km_japan, 'l\n')

# ----------------------------------------------------------------------------------

# Finding the most powerful care by horsepower -------------------------------------
most_powerful_car_all = find_most_powerful_car(read_data)
print('Most Powerful Car by Horsepower:\n', most_powerful_car_all)

europe_cars = read_data.query('origin == "europe"')
most_powerful_car_europe = find_most_powerful_car(europe_cars)
print('\nMost Powerful Car by Horsepower for Europe:\n', most_powerful_car_europe)

usa_cars = read_data.query('origin == "usa"')
most_powerful_car_usa = find_most_powerful_car(usa_cars)
print('\nMost powerful car by horsepower for USA:\n', most_powerful_car_usa)

jap_cars = read_data.query('origin == "japan"')
most_powerful_car_jap = find_most_powerful_car(jap_cars)
print('\nMost powerful car by horsepower for Japan:\n', most_powerful_car_jap)

#  ----------------------------------------------------------------------------------

# Most powerful car by mpg in all cars ---------------------------------------------
best_car_all = find_most_powerful_car_by_mpg(read_data)
print('\nMost powerful car by mpg:\n', best_car_all)

best_car_europe = find_most_powerful_car_by_mpg(europe_cars)
print('\nMost powerful car by mpg for Europe:\n', best_car_europe)

best_car_usa = find_most_powerful_car_by_mpg(usa_cars)
print('\nMost powerful car by mpg for USA:\n', best_car_usa)

best_car_jap = find_most_powerful_car_by_mpg(jap_cars)
print('\nMost powerful car by mpg for Japan:\n', best_car_jap)
#  ----------------------------------------------------------------------------------

