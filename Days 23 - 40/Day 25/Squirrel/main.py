with open("weekly_weather.csv") as file:
    data = file.readlines()
print(data)

import csv

with open("weekly_weather.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] != 'Temperature':
            temperatures.append(int(row[1]))
    # print(temperatures)
import pandas
data = pandas.read_csv("weekly_weather.csv")
# print(data["Temperature"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["Temperature"].to_list()
# print(temp_list)
# summary = 0
# for i in temp_list:
#     summary += i
# summary = sum(temp_list)
# print("Average: ", summary / len(temp_list))
# print(data["Temperature"].max())
# print(data.Condition)
max_temp = data.Temperature.max()
# print(data[data.Temperature == max_temp])
monday = data[data.Day == "Monday"]
print(monday.Temperature * 1.8 + 32)

new_data_dict = {
    "students": ["Amy", "Jimmy", "Umar"],
    "scores": [23,78,39]
}
new_data = pandas.DataFrame(new_data_dict)
new_data.to_csv("new_data.csv")
print(new_data)
