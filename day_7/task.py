# Day 4 - Hang Man
import random

def replace_by_index(word, position, guess):
    # Convert a string in list
    word_list = list(word)
    
    # Replace the character on specific position
    word_list[position] = guess
    
    # Come back List to string
    return ''.join(word_list)

# Picking a Random Words and Checking answers
word_list = ["aardvark", "baboon", "camel"]
errors_list = [
"""
 +-----+
 |     |
 0     |
       |
       |
       |
==========
""",
"""
 +-----+
 |     |
 0     |
/      |
       |
       |
==========
""",
"""
 +-----+
 |     |
 0     |
/|     |
       |
       |
==========
""",
"""
 +-----+
 |     |
 0     |
/|\\    |
       |
       |
==========
""",
"""
 +-----+
 |     |
 0     |
/|\\    |
/      |
       |
==========
""",
"""
 +-----+
 |     |
 0     |
/|\\    |
/ \\    |
       |
========== 
"""

]

chosen_word = random.choice(word_list).lower()
print(chosen_word)

# Replacing blanks with guesses
secret_word = ''
for letter in chosen_word: 
    secret_word += '_'

times_error = 1
finish_word = False
while times_error <= 6 and not finish_word:
    guess = input('Guess a letter: ').lower()
    position = 0
    have_error = True
    
    if(guess in secret_word):
        print('You already choice this letter. Think again')
    else:
        for letter in chosen_word: 
            if(guess == letter): 
                secret_word = replace_by_index(secret_word, position, guess)
                have_error = False
            
            position += 1
        
        if have_error:
            
            print('\n Error letter \n')
            print(errors_list[times_error - 1])
            times_error += 1

        if(chosen_word == secret_word):
            finish_word = True
        print("Secret word: " + secret_word)
    

if times_error > 6:
    print('You Lose. The word is: ' + chosen_word)
elif finish_word: 
    print('You Win. The word is: ' + chosen_word)
else:
    print('Unexperct action')