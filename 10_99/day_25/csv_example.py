import csv
from pathlib import Path

class Temperature:
    def __init__(self, day, temp, condition) -> None:
        self.day = day
        self.temp = temp
        self.condition = condition
        
    def toString(self):
        return f'Day: {self.day}, Temperature was {self.temp} and condition was {self.condition}'

file_path = Path(__file__).parent / "weather_data.csv" 
with open(file_path) as data_file:
    data = csv.reader(data_file)
    temperatures = []
    jump_header = 0
    for row in data:
        if jump_header == 0:
            jump_header += 1
        else:
            temperature = Temperature(day=row[0],temp=row[1], condition=row[2])
            temperatures.append(temperature)
        
    for item in temperatures:
        print(item.toString())