# ToDo  исправить проверку результата - перемешивание списков ответов.
import json
from random import shuffle
from typing import Optional, Union
from datetime import datetime
# подключаем модуль с направляющими линиями
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
# подключаем необходимые виджеты
from PyQt5.QtWidgets import (QApplication, QInputDialog, QHBoxLayout, QRadioButton, QWidget,
                             QPushButton, QLabel, QVBoxLayout, QGroupBox, QMessageBox, QButtonGroup)

win_width, win_height = 900, 500
start_x, start_y = 900, 70
data_quiz_filename = "data.json"


class User:
    def __init__(self, name, lastname) -> None:
        self.name = name
        self.lastname = lastname

    def __str__(self) -> str:
        return f"{self.name} {self.lastname}".title()


class Question:
    def __init__(self, question, right_answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.right_answer = right_answer
        self.answers = [right_answer, wrong_ans1, wrong_ans2, wrong_ans3]

    def get_data(self):
        return self.question, self.answers


class DataQuiz:
    def start(self):
        self.load_data()
        self.current_number = -1
        self.n_right = 0
        self.n_questions = 0

    def load_data(self):
        """Чтение вопросы из json"""
        try:
            with open(data_quiz_filename, "r", encoding="utf-8") as file:
                questions = json.load(file)
        except:
            questions = {
                "Вопрос1":
                    ["Правильный ответ", "Неверный ответ1", "Неверный ответ2", "Неверный ответ3"],
                "Вопрос2":
                    ["Правильный ответ", "Неверный ответ1", "Неверный ответ2", "Неверный ответ3"],
                "Вопрос3":
                    ["Правильный ответ", "Неверный ответ1", "Неверный ответ2", "Неверный ответ3"]}
        self.questions_numbers = list(range(len(questions)))
        shuffle(self.questions_numbers)  # перемешиваем индексы вопросов в случайном порядке
        self.questions = list()
        for question in questions:
            self.questions.append(Question(question, *questions[question]))

    def get_next_question(self):
        if len(self.questions_numbers) > 0:
            self.n_questions += 1
            self.current_number = self.questions_numbers.pop()
            return self.questions[self.current_number].get_data()
        return None, None

    def set_answer(self, answer):
        if self.current_number > -1 and self.questions[self.current_number].right_answer == answer:
            self.n_right += 1

    def get_result(self):
        return f"Правильный ответов {self.n_right} из {self.n_questions}"


class Window(QWidget):
    def __init__(self, parent: Optional['QWidget'] = None,
                 flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> None:
        # вызов конструктора родительского класса
        super().__init__(parent=parent, flags=flags)
        # устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.user = self.get_user()
        self.set_appear()
        self.create_widgets()
        self.layout_widgets()
        self.connects()
        self.data = DataQuiz()
        self.start()

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
        self.RadioGroup = QButtonGroup()  # это для группировки переключателей, чтобы управлять их поведением
        self.RadioGroup.addButton(self.btn1)
        self.RadioGroup.addButton(self.btn2)
        self.RadioGroup.addButton(self.btn3)
        self.RadioGroup.addButton(self.btn4)
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
        self.btn.clicked.connect(self.check_answer)

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

    def show_question(self):
        question, answers = self.data.get_next_question()
        if not question is None:
            # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
            self.RadioGroup.setExclusive(False)
            self.btn1.setChecked(False)
            self.btn2.setChecked(False)
            self.btn3.setChecked(False)
            self.btn4.setChecked(False)
            # вернули ограничения, теперь только одна радиокнопка может быть выбрана
            self.RadioGroup.setExclusive(True)
            shuffle(answers)
            self.question.setText(question)
            self.btn1.setText(answers[0])
            self.btn2.setText(answers[1])
            self.btn3.setText(answers[2])
            self.btn4.setText(answers[3])
        else:
            self.show_result()

    def check_answer(self):
        if self.btn.text() == "Ответить":
            answer = None
            if self.btn1.isChecked():
                answer = self.btn1.text()
            elif self.btn2.isChecked():
                answer = self.btn2.text()
            elif self.btn3.isChecked():
                answer = self.btn3.text()
            elif self.btn4.isChecked():
                answer = self.btn4.text()
            if not answer is None:
                self.data.set_answer(answer)
                self.show_question()
            else:
                QMessageBox.warning(self, "Уведомление", "Выбери один из вариантов ответов!")
        else:
            self.start()

    def show_result(self):
        self.answers.hide()
        self.btn.setText("Попробовать еще раз")
        result = self.data.get_result()
        self.question.setText(f"Вы прошли викторину с результатом:\n{result}")
        self.save_result(result)

    def start(self):
        self.data.start()
        self.btn.setText("Ответить")
        self.answers.show()
        self.show_question()

    def save_result(self, result):
        with open("result.log", "a", encoding="utf-8") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - {self.user} - результат {result}")


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
    # создаём объект приложения
    app = QApp([])
    # создаём объект главного окна
    my_win = Window()
    # даём команду окну показаться
    my_win.show()
    # Оставляет приложение открытым, пока не будет нажата кнопка выхода
    app.exec_()


main()
