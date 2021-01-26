
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
                             QPushButton, QListWidget, QLineEdit, QTextEdit,
                             QInputDialog, QFormLayout)

import sys
import json

file_name = 'notes_data.json'

def create_json(notes):
    '''Заметки в json'''
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def open_json():
    '''Заметки из json'''
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)

def start():
    global notes
    notes = {
        'Добро пожаловать!': {
            'текст': 'Это самое лучшее приложение для заметок в мире!',
            'теги': ['добро', 'инструкция']
        }
    }
    create_json(notes)

def main():
    global notes_win, notes

    def widgets():
        global notes_list, notes_label_list, note_create_button, note_del_button, note_save_button
        global field_tag, field_text, add_button, del_button, search_button, tags_list, tags_label_list

        notes_list = QListWidget()
        notes_label_list = QLabel('Список заметок')

        note_create_button = QPushButton('Создать заметку')
        note_del_button = QPushButton('Удалить заметку')
        note_save_button = QPushButton('Сохранить заметку')

        field_text = QTextEdit()

        field_tag = QLineEdit('')
        field_tag.setPlaceholderText('Введите тег')
        add_button = QPushButton('Добавить к заметке')
        del_button = QPushButton('Открепить от заметки')
        search_button = QPushButton('Искать заметки по тегу')
        tags_list = QListWidget()
        tags_label_list = QLabel('Список тегов')

    def layout_widgets():
        global notes_win
        notes_layout = QHBoxLayout()

        col1 = QVBoxLayout()
        col1.addWidget(field_text)

        col2 = QVBoxLayout()
        col2.addWidget(notes_label_list)
        col2.addWidget(notes_list)

        row1 = QHBoxLayout()
        row1.addWidget(note_create_button)
        row1.addWidget(note_del_button)

        row2 = QHBoxLayout()
        row2.addWidget(note_save_button)

        col2.addLayout(row1)
        col2.addLayout(row2)

        col2.addWidget(tags_label_list)
        col2.addWidget(tags_list)
        col2.addWidget(field_tag)

        row3 = QHBoxLayout()
        row3.addWidget(add_button)
        row3.addWidget(del_button)

        row4 = QHBoxLayout()
        row4.addWidget(search_button)

        col2.addLayout(row3)
        col2.addLayout(row4)

        notes_layout.addLayout(col1, stretch=2)
        notes_layout.addLayout(col2, stretch=1)
        notes_win.setLayout(notes_layout)

    def note_show():
        global notes, notes_list, field_text, tags_list
        key = notes_list.selectedItems()[0].text()
        print(key)
        field_text.setText(notes[key]['текст'])
        tags_list.clear()
        tags_list.addItems(notes[key]['теги'])

    def note_add():
        global notes, tags_list, notes_list
        name_note, ok = QInputDialog.getText(notes_win, 'Добавить заметку', 'Название заметки: ')

        if ok and name_note != '':
            notes[name_note] = {'текст': '', 'теги': []}
            notes_list.addItem(name_note)
            tags_list.addItems(notes[name_note]['теги'])
            print(notes)

    def note_save():
        global notes
        if notes_list.selectedItems():
            key = notes_list.selectedItems()[0].text()
            notes[key]['текст'] = field_text.toPlainText()
            create_json(notes)
            print(notes)
        else:
            print('Заметка для сохранения не выбрана!')  # ToDo Заменить на всплывающее окно

    def note_del():
        global notes, notes_list, tags_list, field_text
        if notes_list.selectedItems():
            key = notes_list.selectedItems()[0].text()
            del notes[key]
            notes_list.clear()
            tags_list.clear()
            field_text.clear()
            notes_list.addItems(notes)
            create_json(notes)
            print(notes)
        else:
            print('Заметка для удаления не выбрана!')  # ToDo Заменить на всплывающее окно

    def tag_add():
        global notes, notes_list, field_tag, tags_list
        if notes_list.selectedItems():
            key = notes_list.selectedItems()[0].text()
            tag = field_tag.text()
            if not tag in notes[key]['теги']:
                notes[key]['теги'].append(tag)
                tags_list.addItem(tag)
                field_tag.clear()
            create_json(notes)
        else:
            print('Заметка для добавления тега не выбрана!')  # ToDo Заменить на всплывающее окно

    def tag_del():
        global notes, notes_list, field_tag, tags_list
        if notes_list.selectedItems():
            key = notes_list.selectedItems()[0].text()
            tag = tags_list.selectedItems()[0].text()
            notes[key]['теги'].remove(tag)
            tags_list.clear()
            tags_list.addItems(notes[key]['теги'])
            create_json(notes)
        else:
            print('Тег для удаления не выбран!')  # ToDo Заменить на всплывающее окно

    def tag_search():
        global notes, notes_list, field_tag, tags_list, search_button
        tag = field_tag.text()
        if search_button.text() == 'Искать заметки по тегу' and tag:
            print(tag)
            notes_filtered = {}
            for note in notes:
                if tag in notes[note]['теги']:
                    notes_filtered[note] = notes[note]
            search_button.setText('Сбросить поиск')
            notes_list.clear()
            tags_list.clear()
            notes_list.addItems(notes_filtered)
            print(search_button.text())
        elif search_button.text() == 'Сбросить поиск':
            field_tag.clear()
            notes_list.clear()
            tags_list.clear()
            notes_list.addItems(notes)
            search_button.setText('Искать заметки по тегу')
            print(search_button.text())
        else:
            print('Тег для поиска не выбран!')  # ToDo Заменить на всплывающее окно

    app = QApplication([])
    notes_win = QWidget()
    notes_win.setWindowTitle('Умные заметки')
    notes_win.resize(900, 600)
    
    widgets()  # создаем нужные виджеты
    layout_widgets()  # Привязываем виджеты

    try:
        notes = open_json()
        if notes == {}:
            start()
    except:
        start()

    notes_list.addItems(notes)

    notes_win.show()
    
    notes_list.itemClicked.connect(note_show)
    note_create_button.clicked.connect(note_add)
    note_save_button.clicked.connect(note_save)
    note_del_button.clicked.connect(note_del)

    add_button.clicked.connect(tag_add)
    del_button.clicked.connect(tag_del)
    search_button.clicked.connect(tag_search)

    sys.exit(app.exec_())



main()
