import csv
import pandas as pd

# Reading the data from weather_data
# with open ("weather_data.csv") as path:
#     data = path.readlines()
#     print(type(data))

with open ("weather_data.csv") as path:
    data = csv.reader(path)
    temp = []
    for row in data:
        if row[1] != 'temp':
            temp.append(int(row[1]))