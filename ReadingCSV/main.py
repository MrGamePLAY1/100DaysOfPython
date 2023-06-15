import csv
import pandas as pd

# Reading the data from weather_data
# with open ("weather_data.csv") as path:
#     data = path.readlines()
#     print(type(data))

# with open ("weather_data.csv") as path:
#     data = csv.reader(path)
#     temp = []
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))

data = pd.read_csv("weather_data.csv")
# print(data['temp'])

data_dict = data.to_dict()
temp_list = data['temp'].to_list()

average_temp = sum(temp_list)/len(temp_list)
average = round(average_temp,2)
# print(average)
# print(data_dict)

# Max
max_temp = data['temp'].max()
# print(max_temp)

# Row
# print(data[data.day == 'Monday'])

# print max temp row
# print(data[data.temp == data.temp.max()])

# Creating data frame from scratch
data_dict = {
    'students' : ['Amy', 'James', 'Angela'],
    'scores' : [76, 56, 65]
}

data_frame = pd.DataFrame(data_dict)
print(data_frame)

data_frame.to_csv("new_data.csv")