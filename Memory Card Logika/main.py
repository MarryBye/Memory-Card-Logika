from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from app import app
from card_window import card_widget
from menu_window import menu_widget

WIN_WIDTH, WIN_HEIGHT = 700, 500

window = QMainWindow()
window.setWindowTitle("Memory Card")
window.resize(WIN_WIDTH, WIN_HEIGHT)
window.setMinimumSize(WIN_WIDTH, WIN_HEIGHT)

window_widget = QWidget()
window_layout = QVBoxLayout()

window_layout.addWidget(card_widget)
window_layout.addWidget(menu_widget)

window_widget.setLayout(window_layout)

window.setCentralWidget(window_widget)

window.show()
app.exec()