import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                            QListWidget, QHBoxLayout, QVBoxLayout, QFileDialog)
from PIL import Image

workdir = '' #вводим глобальную переменную

def main():
    def create_widgets():
        """Создаем виджеты для приложения"""
        global lb_image, btn_dir, lw_files, btn_left, btn_right, btn_flip, btn_sharp, btn_bw
        
        lb_image = QLabel("Картинка")
        btn_dir = QPushButton("Выбор папки")
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
        main_win.setLayout(row)

    def chooseWorkdir():
        global workdir #обращаемся к глобальной переменнуой
        workdir = QFileDialog.getExistingDirectory()

    def filter(files, extensions):
        result = []
        for filename in files:
            for ext in extensions:
                if filename.endswith(ext):
                    result.append(filename)
        return result

    def showFilenamesList():
        extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        chooseWorkdir()
        filenames = filter(os.listdir(workdir), extensions)
        lw_files.clear()
        for filename in filenames:
            lw_files.addItem(filename)
    
    app = QApplication([])
    main_win = QWidget()
    main_win.resize(700, 500)
    main_win.setWindowTitle('Easy Editor')

    create_widgets()
    layout_widgets()

    btn_dir.clicked.connect(showFilenamesList)

    main_win.show()
    app.exec_()

main()