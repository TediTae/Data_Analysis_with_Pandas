data = pandas.read_csv("weather_data.csv")

temp_list = data["temp"].to_list()
print(temp_list)
total_temps = 0
  for temps in temp_list:
    total_temps += temps

print(total_temps)
avg_temp = total_temps / len(temp_list)
print(avg_temp)

maximum_value = data["temp"].max()
print(maximum_value)

monday = data[data["day"] == "Monday"]
print(monday)

celsius = monday["temp"]
fahrenheit = (celsius * 1.8) + 32
print(fahrenheit)
