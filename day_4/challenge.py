import random
instruments = [
    'Rock',
    'Paper',
    'Scissors'
]
option_friendly = int(input('What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors: '))

random_enemy = random.randint(0, 2)

print('MyChoice: ' + instruments[option_friendly])
print('Enemy choice: '+ instruments[random_enemy])

if (option_friendly == 0 and instruments[random_enemy] == 'Rock'):
    print('Draw')
elif (option_friendly == 0 and instruments[random_enemy] == 'Paper'):
    print('Lost')
elif (option_friendly == 0 and instruments[random_enemy] == 'Scissors'):
    print('Win')

if (option_friendly == 1 and instruments[random_enemy] == 'Rock'):
    print('Win')
elif (option_friendly == 1 and instruments[random_enemy] == 'Paper'):
    print('Draw')
elif (option_friendly == 1 and instruments[random_enemy] == 'Scissors'):
    print('Lost')
    

if (option_friendly == 2 and instruments[random_enemy] == 'Rock'):
    print('Lost')
elif (option_friendly == 2 and instruments[random_enemy] == 'Paper'):
    print('Win')
elif (option_friendly == 2 and instruments[random_enemy] == 'Scissors'):
    print('Draw')

