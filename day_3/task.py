# Conditional Statements, Logical Operators, Code Blocks and Scope

# IF Or Else
personal_age = int(input("What's your age?"))

if personal_age < 18:
    print("You don't have age to enter")
else:
    print("You have age to enter")
    
"""Comparison operators
    <
    >
    >=
    <=
    ==
    !=
    
    Modulo Operator
    % -> Check Odd or Even
 """
 
print(12 % 2) # 0
print(3 % 2) # 1
print(12 % 3) # 0
print(10 % 3) # 1

## If , Elif and Else
height = int(input('What is your height in cm: '))
age = int(input('What is your age: '))

ticket_value = 0
if height >=120 and age < 12:
    ticket_value = 5
elif height >=120 and (age >= 12 and age <= 18):
    ticket_value = 7
elif height >=120 and (age > 18):
    ticket_value = 12
else:
    print('Sorry you have to grow taller before you can ride')
    
if ticket_value > 0:
    wants_photho = input('Do you want to have a photo take? Type y for Yes and n for No.')
    
    if wants_photho == 'y':
        ticket_value += 3
        
    print("You can to ride the rollecoaster")
    print(f'please pay ${ticket_value}')
    
    """Logical conditions
        AND
        OR
        NOT
    """