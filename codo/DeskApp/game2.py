from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                            QPushButton, QToolTip, QMessageBox, QLineEdit)
from PyQt5.QtGui import QFont, QIntValidator

from random import shuffle
from copy import deepcopy

class Controller:
    def __init__(self):
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8",
                   "9", "10", "11", "12", "13", "14", "15", " "]
        # Создаем список чисел от 1 до 15
        self.result = Controller.get_numbers(numbers)
        shuffle(numbers)
        self.numbers = Controller.get_numbers(numbers)
        # print(self.result)
        # print(self.numbers)

    def get_number(self, row, col):
        return self.numbers[row][col]

    def check_win(self):
        return self.numbers == self.result

    @staticmethod
    def get_numbers(list_num):
        iter_l = iter(list_num)
        result = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append(next(iter_l))
            result.append(row)
        return result

class MyWin(QWidget):
    def __init__(self, *args, **kwargs):
        # вызываем родительский конструктор
        super().__init__(*args, **kwargs)
        self.resize(600, 700)
        self.setWindowTitle('Пятнашки')
        self.buttons = []
        self.controller = Controller()
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
                button = MyButton(row, column, self.controller.get_number(row, column))
                self.buttons.append(button)
                horizontal_line.addWidget(button)  # , alignment=Qt.AlignCenter
            vertical_line.addLayout(horizontal_line)
        self.setLayout(vertical_line)


class MyButton(QPushButton):
    # переопределяем конструктор класса
    def __init__(self, row, column, text, *args, **kwargs):
        # вызываем родительский конструктор
        super().__init__(*args, **kwargs)
        # переопределяем значения по умолчанию
        self.setFixedSize(QSize(148, 148))
        self.setFont(QFont('Arial', 100))
        self.setText(text)
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
