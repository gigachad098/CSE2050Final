import PyQt5


class Question:
    def __init__(self, question_text, answer, answers, answer_comments, image):
        self._question_text = question_text
        self._answer = answer
        self.answers = answers
        self.answer_comments = answer_comments
        self.image = image

    def imagecheck(self):
        return self.image == None

    def get_text(self):
        return self._question_text

    def set_text(self, question_text):
        self._question_text = question_text

    def check_answer(self, answer):
        return answer == self._answer

    def display(self, layout):
        layout.question_label.set_text(self._question_text)
