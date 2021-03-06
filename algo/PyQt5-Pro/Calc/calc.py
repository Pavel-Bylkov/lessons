import math

#подключаем модуль с направляющими линиями
from PyQt5.QtCore import Qt
#подключаем необходимые виджеты
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
                            QGroupBox, QMessageBox)

DISP_SIZE = "0" * 17  # размер дисплея
WIN_X, WIN_Y = 500, 250

# Todo Добавить обработку скобок

class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.config()
        self.init_gui()
        self.connects()
        self.operation = ""
        self.buffer = 0

    def config(self):
        # создаём название главного окна
        self.setWindowTitle('Калькулятор - версия 1.0')
        # задаём размер окна
        self.resize(WIN_X, WIN_Y)
    
    def init_gui(self):
        self.lb_display = QLabel(DISP_SIZE)
        self.lb_display.setFont(QFont("Uroob Bold", 30))
        self.lb_sign = QLabel(" ")
        self.lb_sign.setFont(QFont("Uroob Bold", 30))
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
        self.btn_pow = QPushButton("x^y")
        self.btn_sqrt = QPushButton(chr(8730))
        self.btn_undo = QPushButton("undo")
        self.layout_widgets()

    def layout_widgets(self):
        v_line = QVBoxLayout()
        h_line = QHBoxLayout()
        h_line.addStretch(0)
        h_line.addWidget(self.lb_sign, alignment=Qt.AlignRight)
        h_line.addWidget(self.lb_display, alignment=Qt.AlignLeft)
        h_line.addStretch(0)
        v_line.addLayout(h_line)

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
        row3.addWidget(self.btn_pow, alignment=Qt.AlignCenter)
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

    def connects(self):
        self.btn_0.clicked.connect(lambda: self.add_num("0"))
        # обработчику событий нельзя передать параметры, поэтому используем lambda
        self.btn_1.clicked.connect(lambda: self.add_num("1"))
        self.btn_2.clicked.connect(lambda: self.add_num("2"))
        self.btn_3.clicked.connect(lambda: self.add_num("3"))
        self.btn_4.clicked.connect(lambda: self.add_num("4"))
        self.btn_5.clicked.connect(lambda: self.add_num("5"))
        self.btn_6.clicked.connect(lambda: self.add_num("6"))
        self.btn_7.clicked.connect(lambda: self.add_num("7"))
        self.btn_8.clicked.connect(lambda: self.add_num("8"))
        self.btn_9.clicked.connect(lambda: self.add_num("9"))
        self.btn_point.clicked.connect(lambda: self.add_num("."))
        self.btn_ac.clicked.connect(self.do_ac)
        self.btn_undo.clicked.connect(self.do_undo)
        self.btn_devision.clicked.connect(lambda: self.add_operation("/"))
        self.btn_plus.clicked.connect(lambda: self.add_operation("+"))
        self.btn_minus.clicked.connect(lambda: self.add_operation("-"))
        self.btn_multi.clicked.connect(lambda: self.add_operation("*"))
        self.btn_pow.clicked.connect(lambda: self.add_operation("^"))
        self.btn_run.clicked.connect(self.do_operation)
        self.btn_percent.clicked.connect(self.percent)
        self.btn_plus_minus.clicked.connect(self.plus_minus)
        self.btn_sqrt.clicked.connect(self.do_op_sqrt)

    def do_ac(self):
        self.reset_display()
        self.buffer = 0

    def plus_minus(self):
        if self.lb_sign.text() == " " and self.lb_display.text() != DISP_SIZE:
            self.lb_sign.setText("-")
        else:
            self.lb_sign.setText(" ")
    
    def reset_display(self):
        self.lb_display.setText(DISP_SIZE)
        self.lb_sign.setText(" ")

    def do_undo(self):
        new_text = "0" + self.lb_display.text()[:-1]
        self.lb_display.setText(new_text)

    def add_num(self, num):
        if self.lb_display.text()[1] != "." and self.lb_display.text()[0] == "0":
            if num != "." or "." not in self.lb_display.text():
                new_text = self.lb_display.text()[1:] + num
                self.lb_display.setText(new_text)
    
    def add_operation(self, op):
        self.operation = op
        if self.buffer == 0:
            if "." in self.lb_display.text():
                self.buffer = float(self.lb_display.text())
            else:
                self.buffer = int(self.lb_display.text())
            if self.lb_sign.text() == "-":
                self.buffer *= -1
            self.reset_display()
    
    def do_operation(self):
        if "." in self.lb_display.text():
            number2 = float(self.lb_display.text())
        else:
            number2 = int(self.lb_display.text())
        if self.lb_sign.text() == "-":
            number2 *= -1
        if self.operation == "+":
            result = self.buffer + number2
        elif self.operation == "-":
            result = self.buffer - number2
        elif self.operation == "*":
            result = self.buffer * number2
        elif self.operation == "^":
            result = self.buffer ** number2
        elif self.operation == "/":
            if number2 != 0:
                result = self.buffer / number2
            else:
                result = 0
                QMessageBox.warning(self, "Ошибка", "Делить на ноль нельзя!")
        self.buffer = 0
        self.show_result(result)
    
    def show_result(self, result):
        if result < 0:
            self.lb_sign.setText("-")
            result *= -1
        result = str(result)
        if "." in result and int(result[result.index(".") + 1:]) == 0:
            result = result[:result.index(".")]
        if len(result) > len(DISP_SIZE):
            if "." not in result or result.index(".") >= len(DISP_SIZE):
                self.reset_display()
                QMessageBox.warning(self, "Ошибка",
                f"Результат {self.lb_sign.text()}{result} не поместился на дисплей.")
            else:
                self.lb_display.setText(result[:len(DISP_SIZE)])
        elif len(result) == len(DISP_SIZE):
            self.lb_display.setText(result)
        else:
            diff = len(DISP_SIZE) - len(result)
            self.lb_display.setText("0" * diff + result)
        
    def percent(self):
        self.add_operation("/")
        self.lb_display.setText("100")
        self.do_operation()
    
    def do_op_sqrt(self):
        if "." in self.lb_display.text():
            number2 = float(self.lb_display.text())
        else:
            number2 = int(self.lb_display.text())
        if self.lb_sign.text() == "-":
            QMessageBox.warning(self, "Ошибка",
                f"Число {self.lb_sign.text()}{number2} отрицательное. Корня нет")
        else:
            result = math.sqrt(number2)
            self.buffer = 0
            self.show_result(result)



def main():
    #создаём объект приложения
    app = QApplication([])
    app.setStyleSheet("""
        QLabel { background-color: grey }
        QPushButton {
                border: 2px solid #8f8f91;
                border-radius: 6px;
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                  stop: 0 #f6f7fa, stop: 1 #dadbde);
                min-width: 80px;
                font: bold 25px;
                    }

        QPushButton:pressed {
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #faafaf, stop: 1 #affaaf);
                    }
                    """)
    # создаём объект главного окна
    my_win = MainWindow()

    # даём команду окну показаться
    my_win.show()
    #Оставляет приложение открытым, пока не будет нажата кнопка выхода
    app.exec_()

main()