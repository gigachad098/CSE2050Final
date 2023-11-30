from PyQt5.QtGui import QImage
from choice_question import ChoiceQuestion


class ChoiceImageQuestion(ChoiceQuestion):
    def __init__(self, question_text, answer, choices, answer_comments, image):
        super().__init__(question_text, answer, choices, answer_comments)
        self._image = image

    def set_image(self, img_path):
        self._image = open(img_path, "rb").read()

    def display(self, layout):
        super().display(layout)
        image = QImage()
        image.loadFromData(self._image)
        # add a QLabel for the image
        # add a QLabel for the question
        # add a QFormLayout for the choices

