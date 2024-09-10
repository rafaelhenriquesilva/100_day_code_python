class QuizBrain:
    question_number: int
    question_list: list
    score: int
    
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        
    def still_has_question(self):
        next_question = True
        if (self.question_number >= len(self.question_list)) :
            next_question = False
            
        return next_question
        
    def next_question(self):
        question = self.question_list[self.question_number]
        answer = ''
        self.question_number += 1
        while answer not in ['True', 'False']:
            answer = input(
                f"Q.{self.question_number}: {question.text} (True / False): \n"
            )
            
        self.check_answer(answer)
        
    def check_answer(self, input_answer):
        is_correct = True
        correct_answer = self.question_list[(self.question_number - 1)].answer
        if correct_answer != input_answer:
            is_correct = False
            
        if is_correct == True:
            self.score += 1
            print('You got it right!')
        else:
            print("That's wrong")
            
        print(f'The correct answers was: {correct_answer}')
        print(f"You current score is: {self.score} / {self.question_number} \n")
        
    def result_quiz(self):
        print("You've completed the Quiz")
        print(f"Your final score was: {self.score} / {self.question_number}")
            
        
        