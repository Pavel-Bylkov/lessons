# ToDo Остановились с Каримом на создании функций обработчиков кнопок - вторая часть
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QListWidget, QLineEdit, QTextEdit, QInputDialog,
                             QHBoxLayout, QVBoxLayout, QFormLayout)
import json

file_name = "notes_data.json"


def write_json(data):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, sort_keys=True)


def read_json():
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    def create_widgets():
        global list_notes, list_notes_label, button_note_create
        global button_note_del, button_note_save, field_text
        global button_tag_add, button_tag_del, button_tag_search
        global list_tags, list_tags_label, field_tag

        # виджеты окна приложения
        list_notes = QListWidget()
        list_notes_label = QLabel('Список заметок')

        button_note_create = QPushButton('Создать заметку')  # появляется окно с полем "Введите имя заметки"
        button_note_del = QPushButton('Удалить заметку')
        button_note_save = QPushButton('Сохранить заметку')
        field_text = QTextEdit()

        field_tag = QLineEdit('')
        field_tag.setPlaceholderText('Введите тег...')
        button_tag_add = QPushButton('Добавить к заметке')
        button_tag_del = QPushButton('Открепить от заметки')
        button_tag_search = QPushButton('Искать заметки по тегу')
        list_tags = QListWidget()
        list_tags_label = QLabel('Список тегов')

    def layout_widgets():
        # расположение виджетов по лэйаутам
        layout_notes = QHBoxLayout()
        col_1 = QVBoxLayout()
        col_1.addWidget(field_text)

        col_2 = QVBoxLayout()
        col_2.addWidget(list_notes_label)
        col_2.addWidget(list_notes)
        row_1 = QHBoxLayout()
        row_1.addWidget(button_note_create)
        row_1.addWidget(button_note_del)
        row_2 = QHBoxLayout()
        row_2.addWidget(button_note_save)
        col_2.addLayout(row_1)
        col_2.addLayout(row_2)

        col_2.addWidget(list_tags_label)
        col_2.addWidget(list_tags)
        col_2.addWidget(field_tag)
        row_3 = QHBoxLayout()
        row_3.addWidget(button_tag_add)
        row_3.addWidget(button_tag_del)
        row_4 = QHBoxLayout()
        row_4.addWidget(button_tag_search)

        col_2.addLayout(row_3)
        col_2.addLayout(row_4)

        layout_notes.addLayout(col_1, stretch=2)
        layout_notes.addLayout(col_2, stretch=1)
        notes_win.setLayout(layout_notes)

    '''Функционал приложения'''
    def show_note():
        """получаем текст из заметки с выделенным названием и отображаем его в поле редактирования"""
        key = list_notes.selectedItems()[0].text()
        field_text.setText(notes[key]["текст"])
        list_tags.clear()
        list_tags.addItems(notes[key]["теги"])

    def add_note():
        note_name, ok = QInputDialog.getText(notes_win, "Добавить заметку", "Название заметки: ")
        if ok and note_name != "":
            notes[note_name] = {"текст": "", "теги": []}
            list_notes.addItem(note_name)
            list_tags.addItems(notes[note_name]["теги"])
            print(notes)

    def save_note():
        if list_notes.selectedItems():
            key = list_notes.selectedItems()[0].text()
            notes[key]["текст"] = field_text.toPlainText()
            write_json(notes)
            print(notes)
        else:
            print("Заметка для сохранения не выбрана!")  # ToDo Добавить оповещение пользователя

    def del_note():
        if list_notes.selectedItems():
            key = list_notes.selectedItems()[0].text()
            del notes[key]
            list_notes.clear()
            list_tags.clear()
            field_text.clear()
            list_notes.addItems(notes)
            write_json(notes)
            print(notes)
        else:
            print("Заметка для удаления не выделена!")  # ToDo Добавить оповещение пользователя

    '''Работа с тегами заметки'''
    def add_tag():
        if list_notes.selectedItems():
            key = list_notes.selectedItems()[0].text()
            tag = field_tag.text()
            if tag != "" and tag not in notes[key]["теги"]:
                notes[key]["теги"].append(tag)
                list_tags.addItem(tag)
                field_tag.clear()
                write_json(notes)
                print(notes)
            elif tag == "":
                print("Поле Введите тег - пустое!")  # ToDo Добавить оповещение пользователя
        else:
            print("Заметка для добавления тега не выделена!")  # ToDo Добавить оповещение пользователя

    def del_tag():
        if list_tags.selectedItems():
            key = list_notes.selectedItems()[0].text()
            tag = list_tags.selectedItems()[0].text()
            notes[key]["теги"].remove(tag)
            list_tags.clear()
            list_tags.addItems(notes[key]["теги"])
            write_json(notes)
        else:
            print("Тег для удаления не выделен!")  # ToDo Добавить оповещение пользователя

    def search_tag():
        print(button_tag_search.text())
        tag = field_tag.text()
        if button_tag_search.text() == "Искать заметки по тегу" and tag:
            print(tag)
            notes_filtered = {}  # тут будут заметки с выделенным тегом
            for note in notes:
                if tag in notes[note]["теги"]:
                    notes_filtered[note] = notes[note]
            button_tag_search.setText("Сбросить поиск")
            field_text.clear()
            list_notes.clear()
            list_tags.clear()
            list_notes.addItems(notes_filtered)
            print(button_tag_search.text())
        elif button_tag_search.text() == "Сбросить поиск":
            field_tag.clear()
            list_notes.clear()
            list_tags.clear()
            field_text.clear()
            list_notes.addItems(notes)
            button_tag_search.setText("Искать заметки по тегу")
            print(button_tag_search.text())
        elif tag == "":
            print("Поле Введите тег - пустое!")  # ToDo Добавить оповещение пользователя

    def start_notes():
        try:
            notes = read_json()
            if notes == {}:
                notes = {
                    "Добро пожаловать!": {
                        "текст": "Это самое лучшее приложение для заметок в мире!",
                        "теги": ["добро", "инструкция"]
                    }
                }
                write_json(notes)
        except:
            '''Заметки в json'''
            data = {
                "Добро пожаловать!": {
                    "текст": "Это самое лучшее приложение для заметок в мире!",
                    "теги": ["добро", "инструкция"]
                }
            }

            write_json(data)
            notes = read_json()
        return notes

    """Основная программа и вызов функций обработчиков событий"""
    app = QApplication([])

    '''Интерфейс приложения'''
    # параметры окна приложения
    notes_win = QWidget()
    notes_win.setWindowTitle('Умные заметки')
    notes_win.resize(900, 600)

    create_widgets()
    layout_widgets()

    '''Запуск приложения'''
    # подключение обработки событий
    list_notes.itemClicked.connect(show_note)
    button_note_create.clicked.connect(add_note)
    button_note_save.clicked.connect(save_note)
    button_note_del.clicked.connect(del_note)
    button_tag_add.clicked.connect(add_tag)
    button_tag_del.clicked.connect(del_tag)
    button_tag_search.clicked.connect(search_tag)

    notes = start_notes()
    list_notes.addItems(notes)

    # запуск приложения
    notes_win.show()
    app.exec_()


main()