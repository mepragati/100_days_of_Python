# with open("Day 025\weather_data.csv") as data_list:
#     data = data_list.readlines()
#     print(data)

# import csv

# with open("Day 025\weather_data.csv") as data_list:
#     data = csv.reader(data_list)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature) 

import pandas

data = pandas.read_csv("Day 025\weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# # print(f"Average temp : {sum(temp_list)/len(temp_list)}")

# print(data["temp"].mean())

# print(data["temp"].max())

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]

print((monday.temp*9)/5 +32)