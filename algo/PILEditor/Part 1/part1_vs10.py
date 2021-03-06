import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QListWidget,
                            QHBoxLayout, QVBoxLayout, QFileDialog)

def main():
    def create_widgets():
        """Создаем виджеты для приложения"""
        global lb_image, btn_dir, lw_files, btn_left, btn_right, btn_flip, btn_sharp, btn_bw 
        lb_image = QLabel("Здесь будет картинка")
        btn_dir = QPushButton("Папка")
        lw_files = QListWidget()

        btn_left = QPushButton("Лево")
        btn_right = QPushButton("Право")
        btn_flip = QPushButton("Зеркало")
        btn_sharp = QPushButton("Резкость")
        btn_bw = QPushButton("Ч/Б")
    def layout_widgets():
        """ Привязка виджетов к линиям и главному окну"""
        row = QHBoxLayout()          # Основная строка
        col1 = QVBoxLayout()         # делится на два столбца
        col2 = QVBoxLayout()
        col1.addWidget(btn_dir)      # в первом - кнопка выбора директории
        col1.addWidget(lw_files)     # и список файлов
        col2.addWidget(lb_image, 95) # вo втором - картинка
        row_tools = QHBoxLayout()    # и строка кнопок
        row_tools.addWidget(btn_left)
        row_tools.addWidget(btn_right)
        row_tools.addWidget(btn_flip)
        row_tools.addWidget(btn_sharp)
        row_tools.addWidget(btn_bw)
        col2.addLayout(row_tools)

        row.addLayout(col1, 20)
        row.addLayout(col2, 80)
        win.setLayout(row)

    def chooseWorkdir():
        """Функция выбора рабочей папки"""
        global workdir #обращаемся к глобальной переменнуой
        workdir = QFileDialog.getExistingDirectory()
        if workdir == None or workdir == "":
            return False
        return True

    def filter_files(files, extensions):
        """Функция отбора имён файлов по расширениям"""
        result = []
        for filename in files:
            for ext in extensions:
                if filename.endswith(ext):
                    result.append(filename)
        return result

    def showFilenamesList():
        """Функция-обработчик нажатия на кнопку «Папка».
            Отвечает за выбор папки, отбор файлов и отображение их в виджете."""
        extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
        if chooseWorkdir():
            filenames = filter_files(os.listdir(workdir), extensions)
            lw_files.clear()
            for name in filenames:
                lw_files.addItem(name)

    def showChosenImage():
        if lw_files.selectedItems():
            name = lw_files.selectedItems()[0].text()
            lb_image.setText(name)

    app = QApplication([])
    win = QWidget()
    win.setWindowTitle('Easy Editor')
    win.resize(700, 500) 

    create_widgets()
    layout_widgets()

    lw_files.itemClicked.connect(showChosenImage)
    btn_dir.clicked.connect(showFilenamesList)
    win.show()
    app.exec()
main()