import string
import random

def shuffle_string(s):
    # Convert the string to a list of characters
    characters = list(s)
    
    # Shuffle the list in place
    random.shuffle(characters)
    
    # Join the list back into a string
    return ''.join(characters)

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['@', '#', '$', '%', '*', '(', ')']

print("Welcome to the PyPassword Genrator")
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input(f'How many symbols would you like in your password?\n'))
nr_numbers = int(input('How many numbers would you like in your password?\n'))

password = ''

for time in range(0, nr_letters):
    password += letters[random.randint(0, len(letters) -1)]
    
for time in range(0, nr_symbols):
    password += symbols[random.randint(0, len(symbols) -1)]
    
for time in range(0, nr_numbers):
    password += numbers[random.randint(0, len(numbers) -1)]
    
password = shuffle_string(password)
print(f'Your password is: {password}')