from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                            QPushButton, QToolTip, QMessageBox, QLineEdit)
from PyQt5.QtGui import QFont, QIntValidator

from random import randint


class MyWin(QWidget):
    def __init__(self, *args, **kwargs):
        # вызываем родительский конструктор
        super().__init__(*args, **kwargs)
        self.resize(600, 600)
        self.setWindowTitle('Пятнашки')


def main():
    # создаем приложение
    app = QApplication([])
    # создаем окно
    win = MyWin()
    win.show()
    # главный цикл
    app.exec_()

main()