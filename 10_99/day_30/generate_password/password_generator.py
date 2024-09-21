import string
import random

class GeneratePassword:

 def exec(self):
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['@', '#', '$', '%', '*', '(', ')']

    print("Welcome to the PyPassword Genrator")
    nr_letters = 5#int(input('How many letters would you like in your password?\n'))
    nr_symbols = 5#int(input(f'How many symbols would you like in your password?\n'))
    nr_numbers = 2#int(input('How many numbers would you like in your password?\n'))

    password = ''

    for _ in range(0, nr_letters):
        password += letters[random.randint(0, len(letters) -1)]
        
    for _ in range(0, nr_symbols):
        password += symbols[random.randint(0, len(symbols) -1)]
        
    for _ in range(0, nr_numbers):
        password += numbers[random.randint(0, len(numbers) -1)]
        
    password = self.shuffle_string(password)

    return password
 
 def shuffle_string(self, s):
        # Convert the string to a list of characters
        characters = list(s)
        
        # Shuffle the list in place
        random.shuffle(characters)
        
        # Join the list back into a string
        return ''.join(characters)