# pip install pandas
import pandas
from pathlib import Path
file_path = Path(__file__).parent / "weather_data.csv" 
data = pandas.read_csv(file_path)


# Dataframe and Series
print(type(data))
print(type(data["temp"]))


data_dict = data.to_dict()
print(data_dict)


temp_list = data['temp'].to_list()
print(temp_list)

average = data['temp'].mean()

print(f'Average: {average}')

# Max temp
max_temp = data['temp'].max()
print(max_temp)

# Get data in row
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])

# Transform Celsius in Farenheits

monday = data[data.day == 'Monday']
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Convert dictionary to dataframe
# data = pandas.DataFrame(data_dict)
# To csv
# data.to_csv('name.csv')