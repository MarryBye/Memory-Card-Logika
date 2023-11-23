from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from app import app
from card_window import card_widget
from menu_window import menu_widget

window = QMainWindow()

window_widget = QWidget()
window_layout = QVBoxLayout()

window_layout.addWidget(card_widget)
window_layout.addWidget(menu_widget)

window_widget.setLayout(window_layout)

window.setCentralWidget(window_widget)

window.show()
app.exec()