from PyQt5.QtCore import Qt
#подключаем необходимые виджеты
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QTextEdit, QLabel,
                            QVBoxLayout, QListWidget, QHBoxLayout, QMessageBox,
                            QInputDialog)

import json

file_data = "notes_data.json"

class File:
    def __init__(self, name) -> None:
        self.name = name
        self.data = None
    
    def get_default_note(self) -> dict:
        return {"default note":{"text": "some text",
                                "tags": ["default", "start"]}
                }

    def read_json(self):
        try:
            with open(self.name, "r", encoding="utf-8") as file:
                self.data = json.load(file)
        except:
            self.data = {"default book": self.get_default_note()}
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
        self.connects()

    def config(self):
        # создаём название главного окна
        self.setWindowTitle('Заметки')
        # задаём размер окна
        self.resize(1200, 750)

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
        v_line1.addWidget(self.lw_notebooks, stretch=80)
        v_line1.addWidget(self.btn_add_book, alignment=Qt.AlignCenter)

        v_line2 = QVBoxLayout()
        v_line2.addWidget(self.lb_notes, alignment=Qt.AlignLeft)
        v_line2.addWidget(self.lw_notes, stretch=80)
        v_line2.addWidget(self.btn_add_note, alignment=Qt.AlignCenter)

        v_line3 = QVBoxLayout()
        v_line3.addWidget(self.btn_save, alignment=Qt.AlignRight)
        v_line3.addWidget(self.note_text, stretch=90)

        h_line = QHBoxLayout()
        h_line.addLayout(v_line1, stretch=20)
        h_line.addLayout(v_line2, stretch=20)
        h_line.addLayout(v_line3, stretch=60)
        self.setLayout(h_line)

    def load_data(self):
        """Получаем список блокнотов и отображаем его"""
        self.lw_notebooks.addItems(self.file.data)
        self.lw_notebooks.setCurrentRow(0)  # выбираем первый блокнот в списке
        self.show_notes()
        
    def connects(self):
        self.lw_notebooks.itemClicked.connect(self.show_notes)
        self.btn_add_book.clicked.connect(self.add_book)
        self.lw_notes.itemClicked.connect(self.show_note)
        self.btn_add_note.clicked.connect(self.add_note)
        self.btn_save.clicked.connect(self.note_save)
        #self.note_text

    def show_notes(self):
        """Получаем список заметок и отображаем его"""
        if self.lw_notebooks.selectedItems():
            self.lw_notes.clear()  # очищаем предыдущий список заметок
            notebook = self.lw_notebooks.selectedItems()[0].text()
            self.lw_notes.addItems(self.file.data[notebook])
            self.lw_notes.setCurrentRow(0)
            self.show_note()
        else:
            QMessageBox.warning(self, "Сообщение об ошибке", "Не выбран блокнот!")
    
    def show_note(self):
        """Получаем текст из заметки с выделенным названием и отображаем его в поле редактирования"""
        if self.lw_notebooks.selectedItems():
            notebook = self.lw_notebooks.selectedItems()[0].text()
            if self.lw_notes.selectedItems():
                note = self.lw_notes.selectedItems()[0].text()
                self.note_text.setText(self.file.data[notebook][note]["text"])
            else:
                QMessageBox.warning(self, "Сообщение об ошибке", "Не выбрана заметка!")
        else:
            QMessageBox.warning(self, "Сообщение об ошибке", "Не выбран блокнот!")
    
    def add_book(self):
        name_book, ok = QInputDialog.getText(self, "Добавление блокнота", "Введите название:")
        if ok and name_book != "":
            if name_book not in self.file.data:
                self.file.data[name_book] = self.file.get_default_note()
                self.lw_notebooks.addItem(name_book)
                self.file.write_json()
            else:
                QMessageBox.warning(self, "Сообщение об ошибке", "Блокнот уже создан!")
        elif ok:
            QMessageBox.warning(self, "Сообщение об ошибке", "Название не должно быть пустым!")

    def add_note(self):
        if self.lw_notebooks.selectedItems():
            notebook = self.lw_notebooks.selectedItems()[0].text()
            name_note, ok = QInputDialog.getText(self, "Добавление заметки", "Введите название:")
            if ok and name_note != "":
                if name_note not in self.file.data[notebook]:
                    self.file.data[notebook][name_note] = {"text": "", "tags": []}
                    self.lw_notes.addItem(name_note)
                    self.file.write_json()
                else:
                    QMessageBox.warning(self, "Сообщение об ошибке", "Заметка с этим названием уже есть!")
            elif ok:
                QMessageBox.warning(self, "Сообщение об ошибке", "Название не должно быть пустым!")
        else:
            QMessageBox.warning(self, "Сообщение об ошибке", "Не выбран блокнот для новой заметки!")

    def note_save(self):
        if self.lw_notebooks.selectedItems():
            notebook = self.lw_notebooks.selectedItems()[0].text()
            if self.lw_notes.selectedItems():
                note = self.lw_notes.selectedItems()[0].text()
                self.file.data[notebook][note]["text"] = self.note_text.toPlainText()
                self.file.write_json()
            else:
                QMessageBox.warning(self, "Сообщение об ошибке", "Не выбрана заметка!")
        else:
            QMessageBox.warning(self, "Сообщение об ошибке", "Не выбран блокнот!")


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