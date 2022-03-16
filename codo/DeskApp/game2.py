from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                            QPushButton, QToolTip, QMessageBox, QLineEdit)
from PyQt5.QtGui import QFont, QIntValidator

from random import shuffle


class Controller:
    def __init__(self):
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8",
                   "9", "10", "11", "12", "13", "14", "15", " "]
        # Создаем список чисел от 1 до 15
        self.result = Controller.get_numbers(numbers)
        shuffle(numbers)  # Перемешиваем список случайным образом
        self.numbers = Controller.get_numbers(numbers)
        print(self.result)
        print(self.numbers)

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
                text = self.controller.get_number(row, column)
                button = MyButton(row, column, text)
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
        # if self.pos[0] > 0:
        #     start0 = 1
        # else:
        #     start0 = 0
        start0 = 1 if self.pos[0] > 0 else 0
        start1 = 1 if self.pos[1] > 0 else 0
        end0 = 1 if self.pos[0] < 3 else 0
        end1 = 1 if self.pos[1] < 3 else 0
        for row in range(self.pos[0] - start0, self.pos[0] + end0 + 1):
            for col in range(self.pos[1] - start1, self.pos[1] + end1 + 1):
                if ((row, col) != self.pos
                        and not (self.pos[0] - start0 == row and self.pos[1] - start1 == col)
                        and not (self.pos[0] + end0 == row and self.pos[1] - start1 == col)
                        and not (self.pos[0] - start0 == row and self.pos[1] + end1 == col)
                        and not (self.pos[0] + end0 == row and self.pos[1] + end1 == col)):
                    print(row, col)

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
