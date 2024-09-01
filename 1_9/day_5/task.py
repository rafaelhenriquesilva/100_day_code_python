# day 5: For Loop, Range and Code Blocks

"""
Loops
for item in list_of_items
    # Do something to each item    
"""

fruits = ['Apple', 'Peach', 'Pear']

for fruit in fruits:
    print(fruit)
    
# Highest Score
students_score = [150, 142,185, 120, 171, 184, 24, 59, 68, 199, 78, 65]
total_exam_score = sum(students_score)
sum = 0
max_score = 0
for score in students_score:
    sum += score
    if (score > max_score):
        max_score = score
    
print(f"Total score: {total_exam_score}")
print(f"Total score loop: {sum}")

print(f'Max score:  {max(students_score)}')
print(f'Max score loop:  {max_score}')
    
# Range Function with for loop
for number in range(20, 40):
    print(number)
    
total = 0    
for number in range(1,101):
    total += number
    
print(total)