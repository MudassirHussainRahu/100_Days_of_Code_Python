# CSV ( Comma Saparated Values )
import pandas as pd
import csv


# data = []
# with open("weather-data.csv") as file:
#     lines = file.readlines()


# for line in lines:
#     line = line.strip()
#     data.append(line.split(","))

# print(data)


# read data from csv file and store it in dataframe
data = pd.read_csv("weather-data.csv")

# print temp column as list
print(data["temp"].to_list())

# print average of temp column
print("Average Temp:", data["temp"].mean())

# print max of temp column
print("Max temp:", data["temp"].max())

# print row where day is Monday
print(data[data["day"] == "Monday"])

# print row where temp is max
print(data[ data["temp"]  == data["temp"].max()])


monday = data[data["day"] == "Monday"]
print(monday.condition)

temp = 9*int(monday.temp.iloc[0])/5 + 32
print(f"Temp in Farenhiet is {temp}") 