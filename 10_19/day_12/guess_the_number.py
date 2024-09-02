# Game: Guess the number
# easy - 10 times
# hard - 5 times

import random
def choice_number():
    number = random.randint(1,100) 
    return number

def verify_choice(correct_number: int, choice: int):
    continue_trying = True
    if correct_number == choice:
        continue_trying = False
        print(f'You got it! The answer was {choice}.')
    elif correct_number < choice:
        print('Too high.')
    else:
        print('Too low.')
        
    return continue_trying

def set_lives():
    lives = 0
    difficult = ''
    while difficult not in ['easy', 'hard']:
        difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
        
    if difficult == 'easy':
        lives = 10
    else: 
        lives = 5
        
    return lives

def loop_alternatives(continue_trying: bool, lives: int, random_number):
    while continue_trying == True and lives > 0:
        print(f'You have {lives} attempts remaining to guess the number.')
        alternative = int(input('Make a guess: '))
        continue_trying = verify_choice(correct_number=random_number, choice=alternative)
        lives -= 1
        
    return lives

def verify_end_game(lives: int, random_number: int ):
    if lives == 0:
        print(f"You've run out of guesses, you lose. The number was {random_number}")

def guessing_game():
    print('Welcome to the number Guessing game')
    random_number = choice_number()
    print("I'm thinking of a number between 1 and 100")
    lives = set_lives()
    continue_trying = True

    lives = loop_alternatives(continue_trying, lives, random_number)
        
    verify_end_game(lives, random_number)
        
guessing_game()

