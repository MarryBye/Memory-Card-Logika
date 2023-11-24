from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from app import app
from card_window import card_widget, lbl_question, lbl_result, lbl_result_answer, rbtn_answer1, rbtn_answer2, rbtn_answer3, rbtn_answer4, btn_check_answer, btn_menu, btn_sleep, result_box, answers_box
from menu_window import menu_widget, btn_back, btn_add_question, btn_clear_inputs
from question_mvc import QuestionController, QuestionViewModel, QuestionModel

# Сохранили в переменные размеры окна
WIN_WIDTH, WIN_HEIGHT = 400, 300

# Создали и настроили окно
window = QMainWindow()
window.setWindowTitle("Memory Card")
window.resize(WIN_WIDTH, WIN_HEIGHT)
window.setMinimumSize(WIN_WIDTH, WIN_HEIGHT)

# Создаем виджет, который вставим в наше окно, а также лейаут для него
window_widget = QWidget()
window_layout = QVBoxLayout()

# В этот виджет добавили наше меню и главную страницу
window_layout.addWidget(card_widget)
window_layout.addWidget(menu_widget)

window_widget.setLayout(window_layout)

# Вставили в окно наш виджет
window.setCentralWidget(window_widget)

# Вопросы

q1 = QuestionModel("Question 1", "Answer 1", "Wrong 1", "Wrong 2", "Wrong 3")
q2 = QuestionModel("Question 2", "Answer 2", "Wrong 1", "Wrong 2", "Wrong 3")
q3 = QuestionModel("Question 3", "Answer 3", "Wrong 1", "Wrong 2", "Wrong 3")
q4 = QuestionModel("Question 4", "Answer 4", "Wrong 1", "Wrong 2", "Wrong 3")
q5 = QuestionModel("Question 5", "Answer 5", "Wrong 1", "Wrong 2", "Wrong 3")

question_viewmodel = QuestionViewModel(lbl_question, rbtn_answer1, rbtn_answer2, rbtn_answer3, rbtn_answer4)
questions_controller = QuestionController(question_viewmodel, q1, q2, q3, q4, q5)

# Функции

def show_menu():
    card_widget.hide()
    menu_widget.show()

def show_main():
    card_widget.show()
    menu_widget.hide()
    
def show_result():
    result_box.show()
    answers_box.hide()
    
def show_answers():
    result_box.hide()
    answers_box.show()
    
def check_answer():
    if btn_check_answer.text() == "Check answer":
        if questions_controller.checked_right():
            lbl_result.setText("Right!")
            lbl_result_answer.setText("")
        else:
            lbl_result.setText("Wrong!")
            lbl_result_answer.setText(f"Right answer: {questions_controller.question_now.answer}")
        btn_check_answer.setText("Next question")
        show_result()
    else:
        questions_controller.show_random_question()
        btn_check_answer.setText("Check answer")
        show_answers()

btn_check_answer.clicked.connect(check_answer)
btn_back.clicked.connect(show_main)
btn_menu.clicked.connect(show_menu)

show_main()
show_answers()

window.show()
app.exec()