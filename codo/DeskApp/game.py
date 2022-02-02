from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                            QPushButton, QToolTip, QMessageBox)
from PyQt5.QtGui import QFont

# создаем приложение
app = QApplication([])
# создаем окно
win = QWidget()
win.resize(600, 600)
win.setWindowTitle('Крестики - Нолики')

turn = 1

class MyButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(QSize(195, 195))
        self.setFont(QFont('Arial', 120))
        self.setText(" ")
        self.clicked.connect(self.push)

    def push(self):
        global turn
        if self.text() == " ":
            if turn == 1:
                turn_char = '0'
                turn = 0
            else:
                turn_char = 'X'
                turn = 1
            self.setText(turn_char)


# вертикальная линия для привязки трех горизонтальных
vertical_line = QVBoxLayout()
for _ in range(3):
    horizontal_line = QHBoxLayout()
    for _ in range(3):
        button = MyButton()
        horizontal_line.addWidget(button)  # , alignment=Qt.AlignCenter
    vertical_line.addLayout(horizontal_line)

win.setLayout(vertical_line)

win.show()
# главный цикл
app.exec_()