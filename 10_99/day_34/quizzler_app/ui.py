from tkinter import *
from pathlib import Path
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizView:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('QUIZLER')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            text='Some question',
            width=200,
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(row=1,column=0,columnspan=2, pady=50)
        
        
        true_image_path = Path(__file__).parent / './images/true.png'
        false_image_path = Path(__file__).parent / './images/false.png'
        
        true_image = PhotoImage(file=true_image_path)
        false_image = PhotoImage(file=false_image_path)
        
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_true_awnser)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_false_awnser)
        self.false_button.grid(row=2, column=1)
        self.next_question()
        self.window.mainloop()
        
    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
        
    def check_true_awnser(self):
        awnser = self.quiz.check_answer('True')
        self.give_feedback(awnser)
        
    def check_false_awnser(self):
        awnser = self.quiz.check_answer('False')
        self.give_feedback(awnser)
        
    def give_feedback(self, is_correct: bool):
        if(is_correct):
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.next_question)