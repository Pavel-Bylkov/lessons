from PyQt5.QtCore import Qt
#подключаем необходимые виджеты
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QLabel, QVBoxLayout, QListWidget, QHBoxLayout

import json

file_data = "notes_data.json"

class File:
    def __init__(self, name) -> None:
        self.name = name
        self.data = None
    
    def read_json(self):
        try:
            with open(self.name, "r", encoding="utf-8") as file:
                self.data = json.load(file)
        except:
            self.data = {
                "default book":{
                    "default note":{
                        "text": "some text",
                        "tags": ["default", "start"]
                    }
                }
            }
            self.write_json()
    
    def write_json(self):
        with open(self.name, "w", encoding="utf-8") as file:
            json.dump(self.data, file, sort_keys=True, ensure_ascii=False)

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config()
        self.file = File(file_data)
        self.file.read_json()
        self.init_gui()
        self.load_data()

    def config(self):
        # создаём название главного окна
        self.setWindowTitle('Заметки')
        # задаём размер окна
        self.resize(1200, 850)

    def init_gui(self):
        """ Метод для создания интерфейса - здесь создаются все виджеты"""
        self.lb_notebooks = QLabel("Список блокнотов")
        self.lw_notebooks = QListWidget()
        self.btn_add_book = QPushButton("Добавить блокнот")

        self.lb_notes = QLabel("Список заметок")
        self.lw_notes = QListWidget()
        self.btn_add_note = QPushButton("Добавить заметку")

        self.note_text = QTextEdit()
        self.btn_save = QPushButton("Сохранить")
        self.layout_widgets()

    def layout_widgets(self):
        v_line1 = QVBoxLayout()
        v_line1.addWidget(self.lb_notebooks, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.lw_notebooks, stretch=80, alignment=Qt.AlignCenter)
        v_line1.addWidget(self.btn_add_book, alignment=Qt.AlignCenter)

        v_line2 = QVBoxLayout()
        v_line2.addWidget(self.lb_notes, alignment=Qt.AlignLeft)
        v_line2.addWidget(self.lw_notes, stretch=80, alignment=Qt.AlignCenter)
        v_line2.addWidget(self.btn_add_note, alignment=Qt.AlignCenter)

        v_line3 = QVBoxLayout()
        v_line3.addWidget(self.btn_save, alignment=Qt.AlignRight)
        v_line3.addWidget(self.note_text, stretch=90, alignment=Qt.AlignCenter)

        h_line = QHBoxLayout()
        h_line.addLayout(v_line1, stretch=20)
        h_line.addLayout(v_line2, stretch=20)
        h_line.addLayout(v_line3, stretch=60)
        self.setLayout(h_line)

    def load_data(self):
        """Получаем список блокнотов и отображаем его"""
        self.lw_notebooks.addItems(self.file.data)
        self.lw_notebooks.setCurrentRow(0)
        self.show_notes()
    
    def show_notes(self):
        """Получаем список заметок и отображаем его"""
        if self.lw_notebooks.selectedItems():
            self.lw_notes.clear()
            notebook = self.lw_notebooks.selectedItems()[0].text()
            self.lw_notes.addItems(self.file.data[notebook])
            self.lw_notes.setCurrentRow(0)
            self.show_note()
        else:
            pass  # Добавить уведомление об ошибке
    
    def show_note(self):
        """Получаем текст из заметки с выделенным названием и отображаем его в поле редактирования"""
        if self.lw_notebooks.selectedItems():
            notebook = self.lw_notebooks.selectedItems()[0].text()
            if self.lw_notes.selectedItems():
                note = self.lw_notes.selectedItems()[0].text()
                self.note_text.setText(self.file.data[notebook][note]["text"])
            else:
                pass
        else:
            pass


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