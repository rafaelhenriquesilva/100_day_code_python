import string
import random

class GeneratePassword:

 def exec(self):
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['@', '#', '$', '%', '*', '(', ')']
    nr_letters = random.randint(1,4)
    nr_symbols = random.randint(1,4)
    nr_numbers = random.randint(1,4)

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