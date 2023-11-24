from random import choice, shuffle

DEFAULT_QUESTION = "Question"
DEFAULT_ANSWER = "Answer"
DEFAULT_WRONG = "Wrong answer"

class QuestionModel:
    def __init__(self, question=DEFAULT_QUESTION, answer=DEFAULT_ANSWER, wrong1=DEFAULT_WRONG, wrong2=DEFAULT_WRONG, wrong3=DEFAULT_WRONG):
        self.question = question
        self.answer = answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        
class QuestionController:
    def __init__(self, viewmodel, *questions):
        
        self.viewmodel = viewmodel
        
        self.questions_list = list()
        self.add_questions(*questions)

        self.question_now = self.show_random_question()        

    def add_question(self, new_question):
        self.questions_list.append(new_question)
        
    def add_questions(self, *questions):
        for question in questions:
            self.questions_list.append(question)
        
    def show_random_question(self):
        self.question_now = choice(self.questions_list)
        self.viewmodel.show_question(self.question_now)
        
        return self.question_now
        
    def checked_right(self):
        return self.viewmodel.answer_buttons[0].isChecked()
        
class QuestionViewModel:
    def __init__(self, question_widget, answer1_widget, answer2_widget, answer3_widget, answer4_widget):
        self.question_widget = question_widget
        self.answer_buttons = [answer1_widget, answer2_widget, answer3_widget, answer4_widget]
        
    def show_question(self, question_model):
        shuffle(self.answer_buttons)
        self.question_widget.setText(question_model.question)
        self.answer_buttons[0].setText(question_model.answer)
        self.answer_buttons[1].setText(question_model.wrong1)
        self.answer_buttons[2].setText(question_model.wrong2)
        self.answer_buttons[3].setText(question_model.wrong3)
        