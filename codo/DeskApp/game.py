from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                            QPushButton, QToolTip, QMessageBox, QLineEdit)
from PyQt5.QtGui import QFont, QIntValidator

from random import randint

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

turn = randint(0, 1)
turn_char = '0' if turn == 1 else 'X'
game_map = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

# todo Проверить закрытие окна с выбором партий
# todo Настроить внешний вид всплывающего окна

def restart_game():
    """Перезапуск всей игры"""
    global number_sets, total0, totalX

    number_sets = 5
    totalX = 0
    total0 = 0
    restart_part()
    question.show()
    win.hide()

def restart_part():
    """Презапуск поля для новой партии"""
    global turn, game_map,turn_char

    turn = randint(0, 1)
    turn_char = '0' if turn == 1 else 'X'
    game_map = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
    for button in buttons:
        button.setText(" ")
    label.setText(f"Текущий ход делает {turn_char}")

def end_part(winner):
    global totalX, total0, number_sets

    number_sets -= 1
    if winner == "победили Х":
        totalX += 1
    elif winner == "победили 0":
        total0 += 1
    msg = f"В этой партии {winner} осталось сыграть {number_sets} партий\n"
    msg += f"Текущий счет: Х - {totalX},  0 - {total0}"
    print(msg)
    QMessageBox.information(win, "Результат партии", msg, QMessageBox.Ok)
    if number_sets == 0:
        end_game()
    else:
        restart_part()

def end_game():
    if total0 > totalX:
        winner = "0"
    elif total0 < totalX:
        winner = "X"
    else:
        winner = "Дружба"
    msg = f"В этой серии партий победил {winner}\n"
    msg += f"Со счетом: Х - {totalX},  0 - {total0}"
    print(msg)
    QMessageBox.information(win, "Результат серии партий", msg, QMessageBox.Ok)
    restart_game()


def game_controller(pos):
    """Меняет значение ячейки game_map с 0 или на 1 или на -1
        И при достижении суммы соседних ячеек 3 или -3 фиксировать победу
        """
    global total0, totalX
    global turn, turn_char

    row, column = pos
    if turn_char == 'X':
        game_map[row][column] = 1
    else:
        game_map[row][column] = -1

    # Проверяем сумму по строкам
    for row1 in game_map:
        if sum(row1) == 3:
            end_part("победили Х")
        elif sum(row1) == -3:
            end_part("победили 0")
    # Проверяем сумму по столбцам
    for col in range(3):
        summ = 0
        for row2 in range(3):
            summ += game_map[row2][col]
        if summ == 3:
            end_part("победили Х")
        elif summ == -3:
            end_part("победили 0")
    # Проверяем сумму по диагоналям
    d1 = game_map[0][0] + game_map[1][1] + game_map[2][2]
    d2 = game_map[2][0] + game_map[1][1] + game_map[0][2]
    if d1 == 3 or d2 == 3:
        end_part("победили Х")
    if d1 == -3 or d2 == -3:
        end_part("победили 0")
    # Проверяем на ничью
    cheker_zero = False
    for row2 in range(3):
        for col in range(3):
            if game_map[row2][col] == 0:
                cheker_zero = True
                break
    if not cheker_zero:
        end_part("Ничья!")
    turn = 0 if turn == 1 else 1
    turn_char = '0' if turn == 1 else 'X'
    label.setText(f"Текущий ход делает {turn_char}")

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
        if self.text() == " ":
            self.setText(turn_char)
            game_controller(self.pos)



# вертикальная линия для привязки трех горизонтальных
vertical_line = QVBoxLayout()
label = QLabel(f"Текущий ход делает {turn_char}")
label.setFont(QFont('Arial', 25))
vertical_line.addWidget(label, alignment=Qt.AlignCenter)
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
