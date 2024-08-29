# day 8: Functions with inputs
# Arguments & Parameters

def my_function():
    #Do this
    #Then Do this
    #Finally Do this
    print('example')

# Function allows for the input    
def greet(
    name: str = 'Default'
):
    print('Hello, ' + name)
    print(f'how do you do {name}?')
    print(f"Isn't the weather nice, {name}?")
    
greet('Rafael')

def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")
    
age = 56 # int(input('How many years do you have?'))
life_in_weeks(age)

# Function with more than 1 input  
def greet_with(
    name: str = 'Default',
    location: str = 'São Paulo'
):
    print('Hello, ' + name)
    print(f'how do you do {name}?')
    print(f"Isn't the weather nice in {location}?")
    
greet_with(location='Rio de Janeiro', name='Rafael')
