import PyQt5
from question import Question

class ChoiceQuestion(Question):
    def __init__(self, question_text, answer, choices, answer_comments):
        super().__init__(question_text, answer)
        self._correct = []
        self._choices = choices
        for choice in choices:
            if choice == answer:
                self._correct.append(choice)
        self._answer_comments = answer_comments
        
    def add_choice(self, choice, correct):
        if correct:
            self._correct.append(choice)
        self._choices.append(choice)

    def check_answer(self, answer):
        return answer in self._correct
        
    def set_answer_comments(self, comments):
        self._answer_comments = comments
            
    def display(self, layout):
        super().display(layout)
        for i, choice in enumerate(self._choices):
            layout.choice_buttons[i].setText(choice)
        