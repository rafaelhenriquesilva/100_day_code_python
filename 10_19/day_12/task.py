# Variables Global vs Scope
enemies = 1

def increase_enemies():
    enemies = 2
    print(f'enemies inside function: {enemies}')
    
increase_enemies()
print(f'enemies outside function: {enemies}')

# There is no Block Scope in python
game_level = 3
enemies = ["Skeleton", "Zombies", "Allien"]

if game_level < 5:
    new_enemy = enemies[0]
    
print(new_enemy)

"""
Prime Number Checker

Prime numbers are numbers that can only be cleanly divided by themselves and 1.   

You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.
It should return True or False.

7 is a primer number because it is only divisible by 1 and itself.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

NOTE: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1.

"""

def is_prime(num):
    is_prime_number = True
    numbers_divisible = []
    for number_to_divide in range(1, (num + 1)):
        if num % number_to_divide == 0:
            numbers_divisible.append(number_to_divide)
            
            
    for number_to_divide in numbers_divisible:
        if (number_to_divide != 1 and number_to_divide != num):
            is_prime_number = False
    return is_prime_number
    
print(is_prime(73))
print(is_prime(75))
        
# How to change the global scope
enemies_fix = 1

# Wrong
def increase_enemies_fix():
    global enemies_fix
    enemies_fix += 2
    print(f'enemies_fix inside function 1: {enemies_fix}')
    
# Good
def increase_enemies_fix_2(enemies_fix):
    enemies_fix += 2
    print(f'enemies_fix inside function 2: {enemies_fix}')
    return enemies_fix
    
increase_enemies_fix()
enemies_fix = increase_enemies_fix_2(enemies_fix)
print(f'enemies_fix outside function: {enemies_fix}')

# Global Constants - uppercase
PI = 3.14159
GOOGLE_URL = 'https://www.google.com/'