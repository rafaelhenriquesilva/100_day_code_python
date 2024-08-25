print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')
print("You're at a cross road. Where do you want to go?.")

direction = input('Type "left" or "right": ')
action = ''
if direction == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    action = input('Type "wait" to wait for a boat. Type "swim" to swim across. ')
    
    if(action == 'wait'):
        print('You arrive at the island inharmed. There is a house with 3 doors.')
        door_color = input('One red, one yellow and one blue. Which color do you choose? ')
        
        if door_color == 'red':
            print("It's a room full of fire. Game Over.")
        elif door_color == 'blue':    
            print('You enter a room of beasts. Game Over.')
        elif door_color == 'yellow':
            print('You found the treasure! You Win!')
        else:
            print('Option need to be: "red", "blue" or "yellow"')
        
    elif action ==  'swim': 
        print('You get attacked by an angry trout. Game Over')   
    else:
        print('Option need to be: "wait" or "swim"')
elif direction == 'right':
    print('You fell into a hole. Game over')
else:
    print('Option need to be: "right" or "left"')