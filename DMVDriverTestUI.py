# DMVDriverTestUI

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DMVDriverTestUI(QWidget):

    def __init__(self, questions):  # , questions
        super().__init__()

        # set up main window
        self.setWindowTitle("DMV Driver's Test")
        self.setGeometry(100, 100, 800, 500)

        # store list of questions
        self.questions = questions

        # keep track of current question and number of correct questions
        self.current_question = 0
        self.correct_answers = 0

        self.UI_Components()

    def UI_Components(self):

        # set up question label
        self.question_label = QLabel(self)
        self.question_label.setGeometry(50, 50, 700, 100)
        self.question_label.setAlignment(Qt.AlignCenter)

        # set up radio buttons for choices
        self.choice_buttons = []
        for i in range(4):
            button = QRadioButton(self)
            button.setGeometry(50, 200 + i * 30, 700, 22)
            button.clicked.connect(self.disable_radio_buttons)
            self.choice_buttons.append(button)

        # set up answer comments label
        self.answer_comments_label = QLabel(self)
        self.answer_comments_label.setGeometry(50, 350, 700, 50)
        self.answer_comments_label.setAlignment(Qt.AlignCenter)

        self.display_question()

        # set up next button
        next_question = QPushButton("Next Question", self)
        next_question.setFont((QFont('Arial', 10)))
        next_question.setGeometry(365, 450, 210, 22)
        next_question.clicked.connect(self.next_question)

        # set up quit button
        quit_quiz = QPushButton("Quit Quiz", self)
        quit_quiz.setFont((QFont('Arial', 10)))
        quit_quiz.setGeometry(580, 450, 210, 22)
        quit_quiz.clicked.connect(QApplication.instance().quit)

    def display_question(self):

        # display the current question
        question = self.questions[self.current_question]
        self.question_label.setText(question.get_text())

        # display choices
        for i, choice in enumerate(question.answers):
            self.choice_buttons[i].setText(choice)

    def disable_radio_buttons(self):

        for button in self.choice_buttons:
            if button.isChecked():
                self.check_answer(button.text())

        # disable all radio buttons when one is clicked
        for button in self.choice_buttons:
            button.setDisabled(True)

    def check_answer(self, text):

        # check answer using the check_answer method of the current question
        question = self.questions[self.current_question]
        if question.check_answer(text):
            self.correct_answers += 1

        # display answer comments
        self.answer_comments_label.setText(question.answer_comments)

    def next_question(self):

        # move to next question
        self.current_question += 1

        # reset radio buttons
        for button in self.choice_buttons:
            button.setChecked(False)
            button.setDisabled(False)


        # clear answer comments
        self.answer_comments_label.clear()

        # check if there are more questions
        if self.current_question < len(self.questions) - 1:
            # display the next question
            self.display_question()
        else:
            # display quiz results
            self.question_label.setText(
                f"Quiz completed. Correct Answers: {self.correct_answers}/{len(self.questions)}")
            # disable next button
            sender = self.sender()
            if sender:
                sender.setDisabled(True)
