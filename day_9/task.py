# day 9: Dictionaries & Nesting

"""
    Dictionaries
    key: value
    code: program instructions
        
"""

program_dictionary = {
    "soup": "a liquid dish, typically made by boiling meat, fish, or vegetables, etc., in stock or water.",
    "rice": "a swamp grass which is widely cultivated as a source of food, especially in Asia.",
    
}

empty_dictionary = {}

# Get value by key
print(program_dictionary['soup'])

# Set a new value
program_dictionary["spaghetti"] = "pasta made in long, slender, solid strings."

print(program_dictionary['spaghetti'])

# Edit an item in dictionary
program_dictionary["spaghetti"] = "update value"

print(program_dictionary['spaghetti'])

# Wipe a existing dictionary
# program_dictionary = empty_dictionary
# print(program_dictionary)

# Loop throught a dictionary
for key in program_dictionary:
    print(key + ":" + program_dictionary[key])


"""
Grading Program
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores. 

Write a program that converts their scores to grades.

By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values. 

The final version of the student_grades dictionary will be checked. 

This is the scoring criteria: 

- Scores 91 - 100: Grade = "Outstanding" 

- Scores 81 - 90: Grade = "Exceeds Expectations" 

- Scores 71 - 80: Grade = "Acceptable" 

- Scores 70 or lower: Grade = "Fail"     
"""

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
        
print(student_grades)

# Nesting List and Dictionaries

"""
{
    Key: [List],
    key2: {Dict}
}    
"""

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Stuttgart"],
}

# print Lille on travel log
print(travel_log['France'][1])

nested_list = ['A', 'B', ['C', 'D']]
# print D on nested_list
print(nested_list[2][1])


travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12    
    },
    "Germany":  {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5    
    },
}


# print Stuttgart on travel log
print(travel_log['Germany']['cities_visited'][2])