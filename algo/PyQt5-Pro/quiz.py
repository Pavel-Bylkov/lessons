#подключаем модуль с направляющими линиями
from PyQt5.QtCore import Qt
#подключаем необходимые виджеты
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

win_width, win_height = 400, 200
start_x, start_y = 900, 70

def main():
    def create_widgets():
        global title,  btn
        title = QLabel('')
        btn = QPushButton("Hello")
    def layout_widgets():
        line = QVBoxLayout()
        line.addWidget(title, alignment=Qt.AlignLeft)
        line.addWidget(btn, alignment=Qt.AlignCenter)
        my_win.setLayout(line)
    def connects():
        btn.clicked.connect(hello)
    def hello():
        title.setText("Hello, world!")
    #создаём объект приложения
    app = QApplication([])
    # создаём объект главного окна
    my_win = QWidget()
    # создаём название главного окна
    my_win.setWindowTitle('Моё первое приложение')
    # задаём размер окна
    my_win.resize(win_width, win_height)
    # задаём точку появления окна на экране компьютера
    my_win.move(start_x, start_y)

    create_widgets()
    layout_widgets()
    connects()
    # даём команду окну показаться
    my_win.show()
    #Оставляет приложение открытым, пока не будет нажата кнопка выхода
    app.exec_()

main()