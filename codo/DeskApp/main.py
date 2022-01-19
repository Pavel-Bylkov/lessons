from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                            QPushButton)

# создаем приложение
app = QApplication([])
# создаем окно
win = QWidget()
win.setWindowTitle('Мое приложение')

# добавляем виджеты
label = QLabel("Надпись")
button = QPushButton("OK")

# вертикальная линия для привязки
vertical_line = QVBoxLayout()
vertical_line.addWidget(label)
vertical_line.addWidget(button)

# привязываем линию с надписью к окну
win.setLayout(vertical_line)

win.show()
# главный цикл
app.exec_()