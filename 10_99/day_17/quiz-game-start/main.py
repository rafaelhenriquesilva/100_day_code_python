import data
from  question_model import Question
from quiz_brain import QuizBrain

question_data = data.question_data

question_bank: list = []

quiz_brain = QuizBrain(question_bank)

for item in question_data: 
    new_question = Question(text=item["text"], answer=item['answer'])
    question_bank.append(new_question)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

quiz_brain.result_quiz()
