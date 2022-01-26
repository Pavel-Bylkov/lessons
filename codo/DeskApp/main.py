# https://pythonworld.ru/gui/pyqt5-firstprograms.html
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                            QPushButton, QToolTip)
from PyQt5.QtGui import QFont

# создаем приложение
app = QApplication([])
# создаем окно
win = QWidget()
win.resize(900, 600)
win.setWindowTitle('Мое приложение')

# добавляем виджеты
label = QLabel("Надпись")
button = QPushButton("OK")

QToolTip.setFont(QFont('Arial', 10))

win.setToolTip('This is a <b>QWidget</b> widget')
button.setToolTip('This is a <b>QPushButton</b> widget')


# вертикальная линия для привязки
vertical_line = QVBoxLayout()
# горизонтальная линия для привязки
horizontal_line = QHBoxLayout()
horizontal_line.addWidget(label, alignment=Qt.AlignCenter)
# связываем две линии - к вертикальной добавляем горизонтальную
vertical_line.addLayout(horizontal_line)
vertical_line.addWidget(button, alignment=Qt.AlignCenter)

# привязываем линию с надписью к окну
win.setLayout(vertical_line)

win.show()
# главный цикл
app.exec_()