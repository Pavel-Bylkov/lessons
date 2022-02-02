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
game_map = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

def game_controller(pos, turn_char):
    """Меняет значение ячейки game_map с 0 или на 1 или на -1
        И при достижении суммы соседних ячеек 3 или -3 фиксировать победу
        """
    row, column = pos
    if turn_char == 'X':
        game_map[row][column] = 1
    else:
        game_map[row][column] = -1

    # Проверяем сумму по строкам
    for row1 in game_map:
        if sum(row1) == 3:
            print("победили Х")
        elif sum(row1) == -3:
            print("победили 0")
    # Проверяем сумму по столбцам
    for col in range(3):
        summ = 0
        for row2 in range(3):
            summ += game_map[row2][col]
        if summ == 3:
            print("победили Х")
        elif summ == -3:
            print("победили 0")
    # Проверяем сумму по диагоналям


class MyButton(QPushButton):
    # переопределяем конструктор класса
    def __init__(self, row, column, *args, **kwargs):
        # вызываем родительский конструктор
        super().__init__(*args, **kwargs)
        # переопределяем значения по умолчанию
        self.setFixedSize(QSize(195, 195))
        self.setFont(QFont('Arial', 120))
        self.setText(" ")
        self.pos = (row, column)
        # привязываем действие при нажатии на кнопку
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
            game_controller(self.pos, turn_char)


# вертикальная линия для привязки трех горизонтальных
vertical_line = QVBoxLayout()
for row in range(3):
    horizontal_line = QHBoxLayout()
    for column in range(3):
        button = MyButton(row, column)
        horizontal_line.addWidget(button)  # , alignment=Qt.AlignCenter
    vertical_line.addLayout(horizontal_line)

win.setLayout(vertical_line)

win.show()
# главный цикл
app.exec_()