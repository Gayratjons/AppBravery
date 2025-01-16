import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250109.csv")

listed_squirrel_color = data["Primary Fur Color"].to_list()

gray_count = 0
red_count = 0
black_count = 0
for color in listed_squirrel_color:
    if color == "Gray":
        gray_count += 1
    elif color == "Cinnamon":
        red_count += 1
    elif color == "Black":
        black_count += 1
print(f"Black:{black_count}\nRed:{red_count}\nGray:{gray_count}")

new_dict = {}
new_dict["Fur Color"] = ["red","black","gray"]
new_dict["Count"] = [red_count,black_count,gray_count]
new_data = pandas.DataFrame(new_dict)
new_data.to_csv("New_Squirrel.csv")
print(new_dict)