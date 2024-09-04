""" 
        Debugging
        In engineering, debugging is the process of finding the root cause of and workarounds and possible fixes for bugs.

        For software, debugging tactics can involve interactive debugging, control flow analysis, log file analysis,
        monitoring at the application or system level, memory dumps, and profiling.
        Many programming languages and software development tools also offer programs to aid in debugging, known as debuggers.
"""


def my_function():
    for i in range(1,20):
        if(i == 20):
            print('You got it!')
            
my_function()

# Describe the Problem - Write your answers as comment:

# 1 - What is the loop doing?
# Scroll the number in range 1 until 20, if determinated condition print "You got it"

# 2 - What is the function to print "You got it"?
# If number in loop equals 20

# 3 - What are your assuptions abbount the value of i?
# The range 1 until 20, stop in 19, and not pass to condition

import random

positions = ["1","2","3","4","5","6"] # array indexes: 0 until 5 - 6 position
random_position = random.randint(1, 6) # Generate Number 1 until 6
# Correction 
random_position = random.randint(0, 5) # Generate Number 0 until 5, equal array indexes
print(positions[random_position])

# Play computer and Evaluate Each line
year = 1994

# 1994 did not are in two condition

"""
if year > 1980 and year < 1994:
    print("You are a millennial.")
    
elif year > 1994:
    print("You are a Gen Z.")
    
"""

if year > 1980 and year < 1994:
    print("You are a millennial.")
    
elif year >= 1994:
    print("You are a Gen Z.")
    

# Fixing Errors and Watching for red underlines
# Input need to be number
# Search: ValueError: invalid literal for int() with base 10: 'nineteen'
# Use Try block
try:
    age = int(input('How old are you?'))
except ValueError:
    print('You have typed in a an invalid number. Please try again!')
    age = int(input('How old are you?'))

if(age > 18):
    print(f"You can drive at age {age}")
    
# Squash bugs with a print() Statement
word_per_page = 0
pages = int(input('Number of pages: '))
# Use == compare and not get the number of words
# word_per_page == int(input('Number of words per pages: '))
 # Correct
word_per_page = int(input('Number of words per pages: '))

print(f"pages: {pages}")
print(f"word_per_page: {word_per_page}")
total_words = pages * word_per_page
print(total_words)