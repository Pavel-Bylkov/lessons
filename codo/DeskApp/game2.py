from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                            QPushButton, QToolTip, QMessageBox, QLineEdit)
from PyQt5.QtGui import QFont, QIntValidator

from random import randint


class MyWin(QWidget):
    def __init__(self, *args, **kwargs):
        # вызываем родительский конструктор
        super().__init__(*args, **kwargs)
        self.resize(600, 700)
        self.setWindowTitle('Пятнашки')
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        # вертикальная линия для привязки трех горизонтальных
        vertical_line = QVBoxLayout()
        label = QLabel(f"Выбери цифру рядом с пустым полем")
        label.setFont(QFont('Arial', 25))
        vertical_line.addWidget(label, alignment=Qt.AlignCenter)
        for row in range(4):
            horizontal_line = QHBoxLayout()
            for column in range(4):
                button = MyButton(row, column)
                self.buttons.append(button)
                horizontal_line.addWidget(button)  # , alignment=Qt.AlignCenter
            vertical_line.addLayout(horizontal_line)
        self.setLayout(vertical_line)


class MyButton(QPushButton):
    # переопределяем конструктор класса
    def __init__(self, row, column, *args, **kwargs):
        # вызываем родительский конструктор
        super().__init__(*args, **kwargs)
        # переопределяем значения по умолчанию
        self.setFixedSize(QSize(148, 148))
        self.setFont(QFont('Arial', 100))
        self.setText(" ")
        self.pos = (row, column)
        # привязываем действие при нажатии на кнопку
        self.clicked.connect(self.push)

    def push(self):
        pass
        # if self.text() == " ":
        #     self.setText(turn_char)
        #     game_controller(self.pos)

def main():
    # создаем приложение
    app = QApplication([])
    # создаем окно
    win = MyWin()
    win.show()
    # главный цикл
    app.exec_()

main()