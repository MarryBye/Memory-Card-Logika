from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

menu_widget = QWidget()
menu_layout = QVBoxLayout()

# Зона ввода информации про вопрос

question_form_layout = QFormLayout()

input_question = QLineEdit()
input_answer = QLineEdit()
input_wrong1 = QLineEdit()
input_wrong2 = QLineEdit()
input_wrong3 = QLineEdit()

question_form_layout.addRow("Question text: ", input_question)
question_form_layout.addRow("Answer text: ", input_answer)
question_form_layout.addRow("Wrong answer 1 text: ", input_wrong1)
question_form_layout.addRow("Wrong answer 2 text: ", input_wrong2)
question_form_layout.addRow("Wrong answer 3 text: ", input_wrong3)

menu_layout.addLayout(question_form_layout)

# ===========================================

menu_widget.setLayout(menu_layout)