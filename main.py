# with open("weather_data.csv") as file:
#     data = file.read()
#     new_data = data.strip()
#     print(new_data)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# temp_sum = 0
# for _ in temp_list:
#     temp_sum += _
#     avg_temp = temp_sum / len(temp_list)
# print(avg_temp)
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data["condition"])  # Get Data in Columns
# print(data.condition)

# print(data[data.day == "Monday"])  # Get Data in Rows
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print((monday.temp[0] * 9/5) + 32)

# data_dict = {  # Create a dataframe from scratch.
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_list = data["Primary Fur Color"].to_list()
grey_count = data_list.count("Gray")
red_count = data_list.count("Cinnamon")
black_count = data_list.count("Black")

squirrel_count = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, red_count, black_count],
}

data = pandas.DataFrame(squirrel_count)
data.to_csv("squirrel_count.csv")
