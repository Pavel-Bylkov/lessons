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

    def swap_number(self, row1, col1, row2, col2):
        bufer = self.numbers[row2][col2]
        self.numbers[row2][col2] = self.numbers[row1][col1]
        self.numbers[row1][col1] = bufer

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
                button = MyButton(row, column, text, self)
                self.buttons.append(button)
                horizontal_line.addWidget(button)  # , alignment=Qt.AlignCenter
            vertical_line.addLayout(horizontal_line)
        self.setLayout(vertical_line)

    def get_btn(self, row, col):
        for btn in self.buttons:
            if btn.pos == (row, col):
                return btn
        return None

    def get_btn_space(self, list_neib):
        for btn in self.buttons:
            if btn.pos in list_neib and btn.text() == ' ':
                return btn
        return None

    @staticmethod
    def get_neib(row, col):
        list_neib = []
        if row - 1 >= 0:
            list_neib.append((row - 1, col))
        if col - 1 >= 0:
            list_neib.append((row, col - 1))
        if col + 1 <= 3:
            list_neib.append((row, col + 1))
        if row + 1 <= 3:
            list_neib.append((row + 1, col))
        return list_neib

    def swap(self, row, col):
        list_neib = self.get_neib(row, col)  # получаем список координат соседей
        btn1 = self.get_btn(row, col)  # получаем ссылку на кнопку куда кликнули
        btn2 = self.get_btn_space(list_neib)  # получаем ссылку на кнопку с пустой ячейкой
        if btn1 is not None and btn2 is not None:
            row2, col2 = btn2.pos
            self.controller.swap_number(row, col, row2, col2)
            text = self.controller.get_number(row, col)
            btn1.setText(text)
            text = self.controller.get_number(row2, col2)
            btn2.setText(text)
            if self.controller.check_win():
                print("Finish!!!")


class MyButton(QPushButton):
    # переопределяем конструктор класса
    def __init__(self, row, column, text, main_win, *args, **kwargs):
        # вызываем родительский конструктор
        super().__init__(*args, **kwargs)
        # сохраняем ссылку на главное окно
        self.main_win = main_win
        # переопределяем значения по умолчанию
        self.setFixedSize(QSize(148, 148))
        self.setFont(QFont('Arial', 100))
        self.setText(text)
        self.pos = (row, column)
        # привязываем действие при нажатии на кнопку
        self.clicked.connect(self.push)

    def push(self):
        self.main_win.swap(self.pos[0], self.pos[1])


def main():
    # создаем приложение
    app = QApplication([])
    # создаем окно
    win = MyWin()
    win.show()
    # главный цикл
    app.exec_()


main()
