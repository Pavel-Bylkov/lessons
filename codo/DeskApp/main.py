# https://pythonworld.ru/gui/pyqt5-firstprograms.html
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                            QPushButton, QToolTip, QMessageBox)
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
button_for_msg = QPushButton("Всплывающее окно")

# Устанавливаем всплывающие подсказки для окна и кнопки
QToolTip.setFont(QFont('Arial', 10))
win.setToolTip('This is a <b>QWidget</b> widget')
button.setToolTip('This is a <b>QPushButton</b> widget')
label.setToolTip('This is a <b>QLabel</b> widget')

# вертикальная линия для привязки
vertical_line = QVBoxLayout()
# горизонтальная линия для привязки
horizontal_line = QHBoxLayout()
horizontal_line.addWidget(label, alignment=Qt.AlignCenter)
# связываем две линии - к вертикальной добавляем горизонтальную
vertical_line.addLayout(horizontal_line)

horizontal_line2 = QHBoxLayout()
horizontal_line2.addWidget(button, alignment=Qt.AlignCenter)
horizontal_line2.addWidget(button_for_msg, alignment=Qt.AlignCenter)
vertical_line.addLayout(horizontal_line2)

# привязываем линию с надписью к окну
win.setLayout(vertical_line)


# добавляем вызов функций при действиях с виджетами
def button_click():
    if label.text() == "Надпись":
        label.setText("Кнопка нажата")
        button.setText("Вернуть Надпись")
    else:
        label.setText("Надпись")
        button.setText("Ок")


def question():
    reply = QMessageBox.question(win, 'Message',
                                 "У тебя все хорошо?", QMessageBox.Yes |
                                 QMessageBox.No, QMessageBox.Yes)
    if reply == QMessageBox.Yes:
        win.setWindowTitle('Сегодня хороший день')
    else:
        win.setWindowTitle('Бывало и по лучше')


button.clicked.connect(button_click)
button_for_msg.clicked.connect(question)

win.show()
# главный цикл
app.exec_()