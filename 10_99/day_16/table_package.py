# Install pip install prettytable
# Doc: https://pypi.org/project/prettytable/
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",
    ["Pikachu","Squirtle","Charmander"])
table.add_column("Type",
    ["Eletric","Water","Fire"])

print(table)