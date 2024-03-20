# with open("weather_data.csv") as data_file: 
#     data = data_file.readlines()
#     print(data)

# import csv 

# with open("weather_data.csv") as data_file: 
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data: 
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
    
#     print(temperature)

import pandas as pd 

data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(data)
# print(data["temp"])

#Converts csv to dictionary
data_dict = data.to_dict
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

avg_temp = data["temp"].mean()

max_temp = data["temp"].max()

print(max_temp)

#Get data in Row
monday_forecast = data[data.day == "Monday"]

max_temp_row = data[data.temp == data.temp.max()]
print(max_temp_row)

monday = data[data.day == "Monday"]
print(monday.condition)

degrees = data["temp"]
for temp in degrees:
    f = round(temp * (5/9)) + 32
    print(f"{f} Degrees")

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
new_data = pd.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data.csv")

