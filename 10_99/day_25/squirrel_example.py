import pandas
from pathlib import Path
file_path = Path(__file__).parent / "2018_Central_Park_Squirrel_Census.csv" 
data = pandas.read_csv(file_path)
grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])


data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
file_path_to_save = Path(__file__).parent / "squirrel_count.csv"
df.to_csv(file_path_to_save)