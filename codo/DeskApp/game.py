from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                            QPushButton, QToolTip, QMessageBox, QLineEdit)
from PyQt5.QtGui import QFont, QIntValidator

# создаем приложение
app = QApplication([])
# создаем окно
win = QWidget()
win.resize(600, 600)
win.setWindowTitle('Крестики - Нолики')

number_sets = 5
totalX = 0
total0 = 0
buttons = []  # список всех кнопок

class Question(QWidget):
    def __init__(self, main, *args, **kwargs):
        # вызываем родительский конструктор
        super().__init__(*args, **kwargs)
        self.main = main
        self.main.hide()
        self.setWindowTitle("Выбор количества партий")
        self.resize(400, 200)

        self.label = QLabel("Сколько партий до победы?")
        self.label.setFont(QFont('Arial', 20))
        self.lineedit = QLineEdit("5")
        self.lineedit.setFont(QFont('Arial', 20))
        self.lineedit.setFixedWidth(40)  # задаем фиксированный размер
        self.lineedit.setValidator(QIntValidator())  # для проверки что ввели число

        self.btn = QPushButton("Ok")
        self.btn.setFont(QFont('Arial', 20))

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addStretch()
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        layout.addWidget(self.lineedit, alignment=Qt.AlignCenter)
        layout.addStretch()
        layout.addWidget(self.btn)

        self.btn.clicked.connect(self.push)

        self.show()

    def push(self):
        global number_sets
        number_sets = self.getValue()
        # скрываем окно ввода
        self.hide()
        self.main.show()

    def getValue(self):
        return int(self.lineedit.text())

turn = 1
game_map = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

# todo Добавить перезапуск всей игры после окончания выбранного количества партий
# todo Проверить закрытие окна с выбором партий

def restart_game():
    """Перезапуск всей игры"""
    global number_sets, total0, totalX

    number_sets = 5
    totalX = 0
    total0 = 0
    question.show()
    win.hide()

def restart_part():
    """Презапуск поля для новой партии"""
    global turn, game_map

    turn = 1
    game_map = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
    for button in buttons:
        button.setText(" ")

def end_part(winner):
    msg = f"В этой партии {winner} осталось сыграть {number_sets} партий\n"
    msg += f"Текущий счет: Х - {totalX},  0 - {total0}"
    print(msg)
    QMessageBox.information(win, "Результат партии", msg, QMessageBox.Ok)

def winX():
    global totalX, number_sets

    number_sets -= 1
    totalX += 1
    end_part("победили Х")
    restart_part()

def win0():
    global total0, number_sets

    number_sets -= 1
    total0 += 1
    end_part("победили 0")
    restart_part()

def game_to_a_draw():
    global number_sets

    number_sets -= 1
    end_part("Ничья!")
    restart_part()

def game_controller(pos, turn_char):
    """Меняет значение ячейки game_map с 0 или на 1 или на -1
        И при достижении суммы соседних ячеек 3 или -3 фиксировать победу
        """
    global total0, totalX
    row, column = pos
    if turn_char == 'X':
        game_map[row][column] = 1
    else:
        game_map[row][column] = -1

    # Проверяем сумму по строкам
    for row1 in game_map:
        if sum(row1) == 3:
            winX()
        elif sum(row1) == -3:
            win0()
    # Проверяем сумму по столбцам
    for col in range(3):
        summ = 0
        for row2 in range(3):
            summ += game_map[row2][col]
        if summ == 3:
            winX()
        elif summ == -3:
            win0()
    # Проверяем сумму по диагоналям
    d1 = game_map[0][0] + game_map[1][1] + game_map[2][2]
    d2 = game_map[2][0] + game_map[1][1] + game_map[0][2]
    if d1 == 3 or d2 == 3:
        winX()
    if d1 == -3 or d2 == -3:
        win0()
    # Проверяем на ничью
    cheker_zero = False
    for row2 in range(3):
        for col in range(3):
            if game_map[row2][col] == 0:
                cheker_zero = True
                break
    if not cheker_zero:
        game_to_a_draw()

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
        buttons.append(button)
        horizontal_line.addWidget(button)  # , alignment=Qt.AlignCenter
    vertical_line.addLayout(horizontal_line)

win.setLayout(vertical_line)

# Создаем окно с выбором количества партий
question = Question(win)

# win.show() - убрали после нажатия Ок
# главный цикл
app.exec_()
