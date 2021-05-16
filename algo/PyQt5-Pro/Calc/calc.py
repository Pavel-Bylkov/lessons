#подключаем модуль с направляющими линиями
from PyQt5.QtCore import Qt
#подключаем необходимые виджеты
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
                            QGroupBox)

class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.config()
        self.init_gui()

    def config(self):
        # создаём название главного окна
        self.setWindowTitle('Калькулятор - версия 1.0')
        # задаём размер окна
        self.resize(500, 250)
    
    def init_gui(self):
        self.lb_display = QLabel("00000000000000000000000")
        self.lb_display.setFont()
        self.gb_buttons = QGroupBox()
        self.btn_bracket_left = QPushButton("(")
        self.btn_bracket_right = QPushButton(")")
        self.btn_ac = QPushButton("AC")
        self.btn_plus_minus = QPushButton("+/-")
        self.btn_percent = QPushButton("%")
        self.btn_devision = QPushButton(chr(247))  # получем символ деления по таблице Юникод
        self.btn_multi = QPushButton("x")
        self.btn_plus = QPushButton("+")
        self.btn_minus = QPushButton("-")
        self.btn_run = QPushButton("=")
        self.btn_point = QPushButton(",")
        self.btn_0 = QPushButton("0")
        self.btn_1 = QPushButton("1")
        self.btn_2 = QPushButton("2")
        self.btn_3 = QPushButton("3")
        self.btn_4 = QPushButton("4")
        self.btn_5 = QPushButton("5")
        self.btn_6 = QPushButton("6")
        self.btn_7 = QPushButton("7")
        self.btn_8 = QPushButton("8")
        self.btn_9 = QPushButton("9")
        self.btn_pov = QPushButton("x^y")
        self.btn_sqrt = QPushButton(chr(8730))
        self.btn_undo = QPushButton(chr(9100))
        self.layout_widgets()

    def layout_widgets(self):
        v_line = QVBoxLayout()
        v_line.addWidget(self.lb_display, alignment=Qt.AlignCenter)

        main_col =QVBoxLayout()
        row1 = QHBoxLayout()
        row1.addWidget(self.btn_bracket_left, alignment=Qt.AlignCenter)
        row1.addWidget(self.btn_ac, alignment=Qt.AlignCenter)
        row1.addWidget(self.btn_plus_minus, alignment=Qt.AlignCenter)
        row1.addWidget(self.btn_percent, alignment=Qt.AlignCenter)
        row1.addWidget(self.btn_devision, alignment=Qt.AlignCenter)
        main_col.addLayout(row1)
        row2 = QHBoxLayout()
        row2.addWidget(self.btn_bracket_right, alignment=Qt.AlignCenter)
        row2.addWidget(self.btn_7, alignment=Qt.AlignCenter)
        row2.addWidget(self.btn_8, alignment=Qt.AlignCenter)
        row2.addWidget(self.btn_9, alignment=Qt.AlignCenter)
        row2.addWidget(self.btn_multi, alignment=Qt.AlignCenter)
        main_col.addLayout(row2)
        row3 = QHBoxLayout()
        row3.addWidget(self.btn_pov, alignment=Qt.AlignCenter)
        row3.addWidget(self.btn_4, alignment=Qt.AlignCenter)
        row3.addWidget(self.btn_5, alignment=Qt.AlignCenter)
        row3.addWidget(self.btn_6, alignment=Qt.AlignCenter)
        row3.addWidget(self.btn_plus, alignment=Qt.AlignCenter)
        main_col.addLayout(row3)
        row4 = QHBoxLayout()
        row4.addWidget(self.btn_sqrt, alignment=Qt.AlignCenter)
        row4.addWidget(self.btn_1, alignment=Qt.AlignCenter)
        row4.addWidget(self.btn_2, alignment=Qt.AlignCenter)
        row4.addWidget(self.btn_3, alignment=Qt.AlignCenter)
        row4.addWidget(self.btn_minus, alignment=Qt.AlignCenter)
        main_col.addLayout(row4)
        row5 = QHBoxLayout()
        row5.addWidget(self.btn_undo, alignment=Qt.AlignCenter)
        row5.addWidget(self.btn_0, alignment=Qt.AlignCenter)
        row5.addWidget(self.btn_point, alignment=Qt.AlignCenter)
        row5.addWidget(self.btn_run, 2, alignment=Qt.AlignAbsolute)
        main_col.addLayout(row5)


        self.gb_buttons.setLayout(main_col)
        v_line.addWidget(self.gb_buttons, alignment=Qt.AlignCenter)
        self.setLayout(v_line)


def main():
    #создаём объект приложения
    app = QApplication([])
    # создаём объект главного окна
    my_win = MainWindow()

    # даём команду окну показаться
    my_win.show()
    #Оставляет приложение открытым, пока не будет нажата кнопка выхода
    app.exec_()

main()