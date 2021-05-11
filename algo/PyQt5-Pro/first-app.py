#подключаем модуль с направляющими линиями
from PyQt5.QtCore import Qt
#подключаем необходимые виджеты
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

#создаём объект приложения
app = QApplication([])
# создаём объект главного окна
my_win = QWidget()

# создаём название главного окна
my_win.setWindowTitle('Моё первое приложение')
# задаём размер окна
my_win.resize(500, 300)
# задаём точку появления окна на экране компьютера
my_win.move(900, 70)

title = QLabel('Text')
btn = QPushButton("Hello")

line = QVBoxLayout()
line.addWidget(title, alignment=Qt.AlignCenter)
line.addWidget(btn, alignment=Qt.AlignCenter)
my_win.setLayout(line)

def hello():
    if title.text() == "Text":
        title.setText("Hello, world!")
    else:
        title.setText("Text") 

btn.clicked.connect(hello)

# даём команду окну показаться
my_win.show()
#Оставляет приложение открытым, пока не будет нажата кнопка выхода
app.exec_()
