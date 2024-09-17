# List Comprehension
# [new_item for item in list]
number_list = [1,2,3,4]
new_list = [n + 1 for n in number_list]

names = ['Rafael', 'Nik', 'Luis', 'Lucas', 'João', 'Alexandre']
short_names = [name for name in names if len(name) < 5]
long_names_upper = [name.upper() for name in names if len(name) >= 5]
print(short_names)
print(long_names_upper)

'''
Squaring Numbers
You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared. 

e.g.

4 * 4 = 16

4 squared equals 16.

**DO NOT** modify the List numbers directly. Try to use List Comprehension instead of a Loop. 

Target Output 

[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025] 

'''
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [item * item for item in numbers]
print(squared_numbers)

'''
Filtering Even Numbers
In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.   

First, use list comprehension to convert the list_of_strings to a list of integers called numbers.   

Then use list comprehension again to create a new list called result.

This new list should only contain the even numbers from the list numbers. 

Again, try to use Python's List Comprehension instead of a Loop. 
'''
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(item) for item in list_of_strings]
result = [item for item in numbers if item % 2 == 0]
print(result)