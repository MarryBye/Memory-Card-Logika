from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

card_widget = QWidget()
card_layout = QVBoxLayout()

# Верхняя часть

header_layout = QHBoxLayout()

btn_menu = QPushButton("Menu")
btn_sleep = QPushButton("Rest")
rest_spinbox = QSpinBox()
rest_spinbox.setValue(30)
lbl_sleep_text = QLabel(" minutes")

header_layout.addWidget(btn_menu)
header_layout.addStretch(1)
header_layout.addWidget(btn_sleep)
header_layout.addWidget(rest_spinbox)
header_layout.addWidget(lbl_sleep_text)

card_layout.addLayout(header_layout)

# ===========================================

# Надпись вопроса

lbl_question = QLabel("Question", alignment=Qt.AlignCenter)

card_layout.addWidget(lbl_question, stretch=1)

# ===========================================

# Варианты ответов

answers_box = QGroupBox("Answers")
answers_box_layout = QHBoxLayout()

rbtn_group = QButtonGroup()

rbtn_answer1 = QRadioButton("Answer 1")
rbtn_answer2 = QRadioButton("Answer 2")
rbtn_answer3 = QRadioButton("Answer 3")
rbtn_answer4 = QRadioButton("Answer 4")

rbtn_group.addButton(rbtn_answer1)
rbtn_group.addButton(rbtn_answer2)
rbtn_group.addButton(rbtn_answer3)
rbtn_group.addButton(rbtn_answer4)

answers_column1_layout = QVBoxLayout()
answers_column1_layout.addWidget(rbtn_answer1)
answers_column1_layout.addWidget(rbtn_answer2)

answers_column2_layout = QVBoxLayout()
answers_column2_layout.addWidget(rbtn_answer3)
answers_column2_layout.addWidget(rbtn_answer4)

answers_box_layout.addLayout(answers_column1_layout)
answers_box_layout.addLayout(answers_column2_layout)

answers_box.setLayout(answers_box_layout)

card_layout.addWidget(answers_box)

# ===========================================

# Результаты теста

result_box = QGroupBox()
result_box_layout = QVBoxLayout()

lbl_result = QLabel("Correct!")
lbl_result_answer = QLabel("Apple")

result_box_layout.addWidget(lbl_result)
result_box_layout.addWidget(lbl_result_answer)

result_box.setLayout(result_box_layout)

card_layout.addWidget(result_box)

# ===========================================

# Кнопка ответа

btn_check_answer = QPushButton("Check answer")

card_layout.addWidget(btn_check_answer)

# ===========================================

card_widget.setLayout(card_layout)