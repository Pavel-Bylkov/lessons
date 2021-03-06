# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QMessageBox,
                             QLabel, QListWidget, QLineEdit, QTextEdit,
                             QInputDialog, QHBoxLayout, QVBoxLayout)
import json
from datetime import datetime

file_name = "notes_data.json"


def write_json(data):
    """Запись заметок в json"""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, sort_keys=True, ensure_ascii=False)


def read_json():
    """Чтение заметок из json"""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        now = datetime.now()
        data = {
        'Добро пожаловать!': {
            'текст': 'Это самое лучшее приложение для заметок в мире!',
            'теги': ['добро', 'инструкция'],
            "дата": f"{now.strftime('%d-%m-%Y')}",
            "время": f"{now.strftime('%H:%M')}"
                            }
                }
        return data


def main():

    def create_widgets():
        """Создаем виджеты для приложения"""
        global list_notes, list_notes_label, button_note_create, button_note_del, button_note_save
        global field_text, list_tags, list_tags_label, field_tag, button_tag_add, button_tag_del
        global button_tag_search, date_time_lable, date_time

        list_notes = QListWidget()
        list_notes_label = QLabel("Список заметок")

        button_note_create = QPushButton("Создать заметку")
        button_note_del = QPushButton("Удалить заметку")
        button_note_save = QPushButton("Сохранить заметку")

        field_text = QTextEdit()
        date_time_lable = QLabel("Дата и Время последнего сохранения:")
        date_time = QLabel("")

        list_tags = QListWidget()
        list_tags_label = QLabel("Список тегов")
        field_tag = QLineEdit("")
        field_tag.setPlaceholderText("Введите тег...")
        button_tag_add = QPushButton("Добавить к заметке")
        button_tag_del = QPushButton("Открепить от заметки")
        button_tag_search = QPushButton("Искать заметки по тегу")

    def layout_widgets():
        """ Привязка виджетов к линиям и главному окну"""
        layout_notes = QHBoxLayout()
        col_1 = QVBoxLayout()
        col_2 = QVBoxLayout()

        col_1.addWidget(field_text)
        row_date = QHBoxLayout()
        row_date.addWidget(date_time_lable)
        row_date.addWidget(date_time)
        col_1.addLayout(row_date)

        col_2.addWidget(list_notes_label)
        col_2.addWidget(list_notes)

        row_1 = QHBoxLayout()
        row_1.addWidget(button_note_create)
        row_1.addWidget(button_note_del)

        col_2.addLayout(row_1)

        col_2.addWidget(button_note_save)

        col_2.addWidget(list_tags_label)
        col_2.addWidget(list_tags)

        col_2.addWidget(field_tag)

        row_2 = QHBoxLayout()
        row_2.addWidget(button_tag_add)
        row_2.addWidget(button_tag_del)

        col_2.addLayout(row_2)

        col_2.addWidget(button_tag_search)

        layout_notes.addLayout(col_1, stretch=2)
        layout_notes.addLayout(col_2, stretch=1)
        notes_win.setLayout(layout_notes)

    '''Функционал приложения'''
    def show_note():
        """Gолучаем текст из заметки с выделенным названием и отображаем его в поле редактирования"""
        key = list_notes.selectedItems()[0].text()
        field_text.setText(notes[key]["текст"])
        date_time.setText(f'{notes[key]["дата"]} {notes[key]["время"]}')
        list_tags.clear()
        list_tags.addItems(notes[key]["теги"])

    def create_note():
        """Запрашивает название новой заметки и создаёт пустую заметку с таким именем"""
        note_name, ok = QInputDialog.getText(notes_win, "Добавить заметку", "Название заметки: ")
        if ok and note_name != "":
            now = datetime.now()
            notes[note_name] = {"текст": "", "теги": [], "дата": f"{now.strftime('%d-%m-%Y')}", "время": f"{now.strftime('%H:%M')}"}
            list_notes.addItem(note_name)
            list_tags.addItems(notes[note_name]["теги"])
            write_json(notes)

    def save_note():
        """Сохраняет текст в выбранную заметку из словаря notes и обновляет файл с данными"""
        if list_notes.selectedItems():
            key = list_notes.selectedItems()[0].text()
            now = datetime.now()
            notes[key]["текст"] = field_text.toPlainText()
            notes[key]["дата"] = f"{now.strftime('%d-%m-%Y')}"
            notes[key]["время"] = f"{now.strftime('%H:%M')}"
            write_json(notes)
        else:
            QMessageBox.warning(notes_win, "Уведомление", "Заметка для сохранения не выбрана!")

    def del_note():
        """Удаляет выбранную заметку из словаря notes, из файла и из виджетов"""
        if list_notes.selectedItems():
            key = list_notes.selectedItems()[0].text()
            del notes[key]
            list_notes.clear()
            list_tags.clear()
            field_text.clear()
            list_notes.addItems(notes)
            write_json(notes)
        else:
            QMessageBox.warning(notes_win, "Уведомление", "Заметка для удаления не выбрана!")

    def add_tag():
        """Добавляет введённый тег в список тегов выделенной заметки"""
        if list_notes.selectedItems():
            key = list_notes.selectedItems()[0].text()
            tag = field_tag.text()
            if tag and tag not in notes[key]["теги"]:
                notes[key]["теги"].append(tag)
                list_tags.addItem(tag)
                field_tag.clear()
                write_json(notes)
        else:
            QMessageBox.warning(notes_win, "Уведомление", "Заметка для добавления тега не выбрана!")

    def del_tag():
        """Удаляет выделенный тег из список тегов выделенной заметки"""
        if list_notes.selectedItems() and list_tags.selectedItems():
            key = list_notes.selectedItems()[0].text()
            tag = list_tags.selectedItems()[0].text()
            notes[key]["теги"].remove(tag)
            list_tags.clear()
            list_tags.addItems(notes[key]["теги"])
            write_json(notes)
        elif not list_notes.selectedItems():
            QMessageBox.warning(notes_win, "Уведомление", "Заметка для удаления тега не выбрана!")
        else:
            QMessageBox.warning(notes_win, "Уведомление", "Тег для удаления не выбран!")

    def search_tag():
        """Составляет список заметок, содержащих введённый тег"""
        tag = field_tag.text()
        if button_tag_search.text() == "Искать заметки по тегу" and tag:
            notes_filtred = {}  # временый словарь для сохранения найденных заметок
            for note in notes:
                print(tag, notes[note]["теги"])
                if tag in notes[note]["теги"]:
                    notes_filtred[note] = notes[note]
            button_tag_search.setText("Сбросить поиск")
            list_notes.clear()
            list_tags.clear()
            field_text.clear()
            list_notes.addItems(notes_filtred)
        elif button_tag_search.text() == "Сбросить поиск":
            list_notes.clear()
            list_tags.clear()
            field_text.clear()
            field_tag.clear()
            list_notes.addItems(notes)
            button_tag_search.setText("Искать заметки по тегу")
        else:
            QMessageBox.warning(notes_win, "Уведомление", "Тег для поиска не указан!")


    app = QApplication([])

    """Интерфейс приложения"""
    notes_win = QWidget()
    notes_win.setWindowTitle("Умные заметки")
    notes_win.resize(900, 600)

    create_widgets()
    layout_widgets()

    notes = read_json()
    list_notes.addItems(notes)

    # делаем привязку к событиям
    list_notes.itemClicked.connect(show_note)
    button_note_create.clicked.connect(create_note)
    button_note_save.clicked.connect(save_note)
    button_note_del.clicked.connect(del_note)
    button_tag_add.clicked.connect(add_tag)
    button_tag_del.clicked.connect(del_tag)
    button_tag_search.clicked.connect(search_tag)

    # запуск приложения
    notes_win.show()
    app.exec_()

main()