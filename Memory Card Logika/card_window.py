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
header_layout.addSpacing(1)
header_layout.addWidget(btn_sleep)
header_layout.addWidget(rest_spinbox)
header_layout.addWidget(lbl_sleep_text)

card_layout.addLayout(header_layout)

# ===========================================

card_widget.setLayout(card_layout)