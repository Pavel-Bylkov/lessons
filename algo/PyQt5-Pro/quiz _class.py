#подключаем модуль с направляющими линиями
from typing import Optional, Union
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
#подключаем необходимые виджеты
from PyQt5.QtWidgets import (QApplication, QInputDialog, QHBoxLayout, QRadioButton, QWidget, 
                                QPushButton, QLabel, QVBoxLayout, QGroupBox, QMessageBox)

win_width, win_height = 900, 500
start_x, start_y = 900, 70
data_quiz_filename = ""

class User():
    def __init__(self, name, lastname) -> None:
        self.name = name
        self.lastname = lastname
    def __str__(self) -> str:
        return f"{self.name} {self.lastname}".title()

class DataQuiz():
    def __init__(self) -> None:
        self.questions = {}
        self.n_allquestions = 0
        self.n_right = 0
        self.n_questions = 0
    def load_data(self):
        pass
    def get_next_question(self):
        pass


class Window(QWidget):
    def __init__(self, parent: Optional['QWidget'] = None,
            flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> None:
        #вызов конструктора родительского класса
        super().__init__(parent=parent, flags=flags)
        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.user = self.get_user()
        self.set_appear()
        self.create_widgets()
        self.layout_widgets()
        self.connects()
    
    def set_appear(self):
        # создаём название главного окна
        self.setWindowTitle('Викторина для ' + str(self.user))
        # задаём размер окна
        self.resize(win_width, win_height)
        # задаём точку появления окна на экране компьютера
        self.move(start_x, start_y)
    def create_widgets(self):
        self.question = QLabel('Здесь будет вопрос')
        self.answers = QGroupBox("Варианты ответов")
        self.btn1 = QRadioButton("Ответ 1")
        self.btn2 = QRadioButton("Ответ 2")
        self.btn3 = QRadioButton("Ответ 3")
        self.btn4 = QRadioButton("Ответ 4")
        self.btn = QPushButton("Ответить")
    def layout_widgets(self):
        line = QVBoxLayout()
        line.addWidget(self.question, alignment=Qt.AlignCenter)
        ans_hline = QHBoxLayout()
        ans_vline1 = QVBoxLayout()
        ans_vline2 = QVBoxLayout()
        ans_vline1.addWidget(self.btn1, alignment=Qt.AlignLeft)
        ans_vline1.addWidget(self.btn2, alignment=Qt.AlignLeft)
        ans_vline2.addWidget(self.btn3, alignment=Qt.AlignLeft)
        ans_vline2.addWidget(self.btn4, alignment=Qt.AlignLeft)
        ans_hline.addLayout(ans_vline1)
        ans_hline.addLayout(ans_vline2)
        self.answers.setLayout(ans_hline)
        line.addWidget(self.answers)
        line.addWidget(self.btn, alignment=Qt.AlignCenter)
        self.setLayout(line)
    def connects(self):
        #self.btn.clicked.connect(self.hello)
        pass
    def get_user(self, deep=0):  # рекурсивный метод, вызывает сам себя при ошибках ввода
        if deep == 5:
            QMessageBox.warning(self, "Уведомление", "Авторизация не пройдена! Программа будет закрыта.")
            exit()
        name, ok = QInputDialog.getText(self, "Авторизация", "Введите имя: ")
        if ok and name != "":
            lastname, ok = QInputDialog.getText(self, "Авторизация", "Введите Фамилию: ")
            if lastname == "":
                QMessageBox.warning(self, "Уведомление", "Фамилия не указана!")
                return self.get_user(deep + 1)
        else:
            QMessageBox.warning(self, "Уведомление", "Имя не указано!")
            return self.get_user(deep + 1)
        return User(name, lastname)

class QApp(QApplication):
    def __init__(self, list_str):
        super().__init__(list_str)
        self.set_fusion_style()

    def set_fusion_style(self):
        self.setStyle("Fusion")

        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, Qt.white)
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        dark_palette.setColor(QPalette.Text, Qt.white)
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, Qt.white)
        dark_palette.setColor(QPalette.BrightText, Qt.red)
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.HighlightedText, Qt.black)

        self.setPalette(dark_palette)

        self.setStyleSheet("QToolTip { color: #ffffff; "
                           "background-color: #2a82da; "
                           "border: 1px solid white; }")
        font = self.font()
        font.setPointSize(14)
        QApplication.instance().setFont(font)

def main():
    #создаём объект приложения
    app = QApp([])
    # создаём объект главного окна
    my_win = Window()
    # даём команду окну показаться
    my_win.show()
    #Оставляет приложение открытым, пока не будет нажата кнопка выхода
    app.exec_()

main()