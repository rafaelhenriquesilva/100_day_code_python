# Day 4: Randomisation and Python Lists
import random
import my_module
# random - número entre 0 e 1
random_number = random.randint(1,10)

print(random_number)

print(my_module.my_favorite_number)

# number 0 - 1
print(random.random())

# random only float number
print(random.uniform(0, 10))

# related random with code
random_head_or_tails = random.randint(0, 1)
if (random_head_or_tails == 0):
    print("Heads")
else:
    print('Tails')
    
# List
states_brazil = ['Sao Paulo', "Rio de Janeiro", "Brasilia"]
states_brazil.extend(['Minas Gerais', 'Goias'])
print(states_brazil)


## Who will pay the bill?
friends = ['Rafael', 'Lucas', 'Nik', 'Luis']
print(friends[random.randint(0, len(friends) - 1)])
print(random.choice(friends))


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])