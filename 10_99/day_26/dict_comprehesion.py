# Dict Comprehension
# new_dict = {new_key: new_value for (key, value) in dict.items()}
import random

names = ['Rafael', 'Nik', 'Luis', 'Lucas', 'João', 'Alexandre']

students_scores = {student: random.randint(1,100) for student in names}
print(students_scores)
passed_students = {student: value for (student, value) in students_scores.items() if value >= 60}
print(passed_students)


