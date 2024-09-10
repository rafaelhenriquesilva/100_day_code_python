import random
# Run in Debug and put the append inside For
def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
    b_list.append(new_item)
    print(b_list)
    
mutate([1,2,3,4,6,7,9,19])