import sys
from PyQt5.QtWidgets import QApplication
from DMVDriverTestUI import DMVDriverTestUI
import XMLParser

#questions = [] # list of question objects
app = QApplication(sys.argv)
questions = XMLParser.parse('florida_drivers_test.xml')
window = DMVDriverTestUI(questions)
window.show()
app.exec_()