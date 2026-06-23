numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Do Not Change the code above 👆
# Write your 1 line code below:
# Write your code above 👆
squared_numbers = [number ** 2 for number in numbers]
even_numbers = [number for number in numbers if number % 2 == 0]
# print(squared_numbers)
# print(even_numbers)


with open("file1.txt") as file:
    data = list(file.readlines())
data_file1 = [int(number.strip()) for number in data]
# print(data_file1)

with open("file2.txt") as file:
    data = list(file.readlines())
data_file2 = [int(number.strip()) for number in data]
# print(data_file2)

combined_list = [number for number in data_file1 if number in data_file2]
# print(combined_list)

weekly_temperature = {
    'Monday': 17,
    'Tuesday': -2,
    'Wednesday': 14,
    'Thursday': -1,
    'Friday': 18,
    'Saturday': 1,
    'Sunday': 13
}

temp_f = {week_day: (temperature * 9/5) + 32 for (week_day,temperature) in weekly_temperature.items()}
print(temp_f)

# --------------------------------------------------------------------------------------------

student_dict = {
    "student": ["Angela", "Umar", "Uthman"],
    "score": [56,76,98]
}
# for (index,row) in student_dict.items():
#     print(index)
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.student)
        print(row.score * 2)