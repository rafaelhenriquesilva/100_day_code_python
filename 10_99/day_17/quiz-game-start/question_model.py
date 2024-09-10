class Question:
    text: str
    answer: str
    
    def __init__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = answer