data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250616.csv")

fur_column = data["Primary Fur Color"]

fur_list = fur_column.to_list()
gray_squirrel = 0
cinnamon_squirrel = 0
black_squirrel = 0

for rows in fur_list:
    if rows == "Gray":
        gray_squirrel += 1
    if rows == "Cinnamon":
        cinnamon_squirrel += 1
    if rows == "Black":
        black_squirrel += 1

# print(gray_squirrel, cinnamon_squirrel, black_squirrel)

new_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel, cinnamon_squirrel, black_squirrel],
}

#This creates new csv file each color with counts of them. Easier to analyse
dataframe = pandas.DataFrame(new_dict)
dataframe.to_csv("squirrel_count")
