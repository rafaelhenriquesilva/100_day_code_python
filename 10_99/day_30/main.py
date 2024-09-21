# FileNotFound
# with open('invalid_file.txt')  as file:
#     file.read()

# Key Error
# invalid_dict = {"key": "value"}
# value = invalid_dict['invalid_key']

# Index Error
# fruit_list = ['Apple', 'Banana']
# invalid_fruit = fruit_list[99]

"""
try: Something tha might cause an exception
except: Do this if there was an exception
else: Do this if there were no exceptions
finally: Do this no matter what happens

"""
from pathlib import Path
file_path = Path(__file__).parent / "invalid_file.txt"
try:
    file = open(file_path)
    animals = ['Pig', 'Cat', 'Dog']
    animals[5]
    numbers_dict = {"one": 1, "two": 2, "three": 3}
    numbers_dict['invalid_key']
except FileNotFoundError:
    file = open(file_path, 'w')
    file.write('Something')
except KeyError as key_error:
    print(f"That key {key_error} does not exist.")
except IndexError as index_error:
    print(f"That index {index_error} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()

# Raising exception - Tratment Specific of error
height = float(input('Height: '))
weight = float(input('Weight: '))

if height > 3:
    raise ValueError('Human Height should not be over 3 meters')

bmi = weight / height ** 2

print(bmi)


"""
KeyError Handling
We've got some buggy code, try running the code. The code will crash and give you a KeyError.

This is because some of the posts in the facebook_posts don't have any "Likes". 

Objective 

Use what you've learnt about exception handling to prevent the program from crashing. 
"""
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2,'Likes': 33,},
    {'Comments': 1, 'Shares': 1, 'Likes': 33,},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        post_like = 0
        try:
            post_like = post['Likes']
        except: 
            post['Likes'] = 0
            
        total_likes = total_likes + post_like
    
    return total_likes


count = count_likes(facebook_posts)
print(count)

