from PyQt5.QtCore import Qt
#подключаем необходимые виджеты
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QListWidget, QHBoxLayout

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config()
        self.init_gui()

    def config(self):
        # создаём название главного окна
        self.setWindowTitle('Заметки')
        # задаём размер окна
        self.resize(1200, 850)

    def init_gui(self):
        """ Метод для создания интерфейса - здесь создаются все виджеты"""
        self.lb_notebooks = QLabel("Список блокнотов")
        self.lw_notebooks = QListWidget()

        v_line = QVBoxLayout()
        v_line.addWidget(self.lb_notebooks, alignment=Qt.AlignLeft)
        v_line.addWidget(self.lw_notebooks, alignment=Qt.AlignCenter)

        h_line = QHBoxLayout()
        h_line.addLayout(v_line)
        self.setLayout(h_line)


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