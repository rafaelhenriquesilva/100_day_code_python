print('Welcome to the tipe calculator! ')
bill = float(input('What was the total bill? '))
percentage = int(input('How much tipe would you like to give? 10, 12, or 15? ')) / 100
number_of_people = int(input('How many people to split the bill? '))
result = ((bill / number_of_people) * (1 + percentage))
print(f'Each person should pay: {result}')
