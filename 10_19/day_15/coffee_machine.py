# Coffee Machine
import main
"""
1 - Make 3 hot flavoues
    Different quantity, coffee and milk

2- coin operate
    Penny - 0.01 cent
    Dime - 10 cents
    Nickel - 5 cents
    Quarter - 25 cents
"""
# Import information
menu = main.MENU
resources = main.resources

def show_resources(resources): 
    print('------ Machine Resources ------')
    for key in resources: 
        print(f"{key}: {resources[key]}")



# Select the drink
def select_drink():
    choice = ''
    while (choice not in ["espresso","latte","cappuccino"]):
        choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    
    return choice


def check_specific_resource(ingredients_to_drink, resource_name, have_resource):
    if ingredients_to_drink.get(resource_name, 0) and (ingredients_to_drink.get(resource_name, 0) > resources.get(resource_name, 0)):
        print(f"Don't have sufficient water, required: {ingredients_to_drink[resource_name]}, quantity: {resources[resource_name]}")
        have_resource = False
    return have_resource

def verify_and_remove_resource(ingredients_to_drink, resources, resource_name):
    if ingredients_to_drink.get(resource_name, 0):
            resources[resource_name] -= ingredients_to_drink[resource_name]
    return resources

def verify_resources(type_drink, resources):
    have_resource = True
    ingredients_to_drink = menu[type_drink]['ingredients']
    list_ingredients = list(resources.keys())
    
    for ingredient in list_ingredients:
        have_resource = check_specific_resource(ingredients_to_drink, ingredient, have_resource)
        
    if have_resource == True:
        for ingredient in list_ingredients:
            resources = verify_and_remove_resource(
                resources=resources,
                ingredients_to_drink=ingredients_to_drink,
                resource_name=ingredient
            )
            
    return {
        "resources": resources,
        "have_resource": have_resource
    }


def get_coin_value(name, price):
    value = float(input(f"How many {name} do you want? {price} "))
    return value

def create_coin(name, value):
    return  {
                    "name":name,
                    "value": value,
                    "quantity": get_coin_value(name, value)
            }

def process_coins(): 
    total = 0
    coins = [
                create_coin(name="Dime", value=0.1),
                create_coin(name="Penny", value=0.01),
                create_coin(name="Nickel", value=0.05),
                create_coin(name="Quarter", value=0.25)
            ]
    
    for data in coins:
        total += data['value'] * data['quantity']
        
    print(total)
        
    return {
        "coins": coins,
        "total": total
    }
    
def finishing_order(dict_coins, type_drink):
    if menu[type_drink]['cost'] > dict_coins['total']:
        print(f"You don't have sufficient money to pay the {type_drink}\n")
    else:
        change_money = dict_coins['total'] - menu[type_drink]['cost']
        print(f"Your order {type_drink} here. Your change: {change_money}.\n")

# Run program    
def run():
    show_resources(resources)
    type_drink = select_drink()
    dict_resources = verify_resources(type_drink, resources)
    show_resources(dict_resources['resources'])
    if(dict_resources['have_resource'] == True):
        dict_coins = process_coins()
        finishing_order(dict_coins=dict_coins, type_drink=type_drink)
        
run()