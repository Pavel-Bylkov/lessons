import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QListWidget,
                             QHBoxLayout, QVBoxLayout, QFileDialog)
from PyQt5.QtGui import QPixmap  # оптимизированная для показа на экране картинка
from PIL import Image


class ImageProcessor():
    def __init__(self):
        """Конструктор класса"""
        self.image = None
        self.dir = ""
        self.filename = ""
        self.save_dir = "Modified"

    def load_image(self):
        self.image_path = os.path.join(workdir, self.filename)
        self.image = Image.open(self.image_path)

    def show_image(self):
        lb_image.hide()
        pixmapimage = QPixmap(self.image_path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

    def show_chosen_image(self):
        if lw_files.currentRow() >= 0:
            self.filename = lw_files.currentItem().text()
            self.load_image()
            self.show_image()

    def do_bw(self):
        self.image = self.image.convert("L")
        self.save_image()
        self.image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.show_image()

    def save_image(self):
        """сохраняет копию файла в подпапке"""
        path = os.path.join(workdir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        new_image_path = os.path.join(path, self.filename)
        self.image.save(new_image_path)


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
        row = QHBoxLayout()  # Основная строка
        col1 = QVBoxLayout()  # делится на два столбца
        col2 = QVBoxLayout()
        col1.addWidget(btn_dir)  # в первом - кнопка выбора директории
        col1.addWidget(lw_files)  # и список файлов
        col2.addWidget(lb_image, 95)  # вo втором - картинка
        row_tools = QHBoxLayout()  # и строка кнопок
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
        global workdir  # обращаемся к глобальной переменнуой
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

    def show_filenames_list():
        """Функция-обработчик нажатия на кнопку «Папка».
            Отвечает за выбор папки, отбор файлов и отображение их в виджете."""
        extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        if chooseWorkdir():
            filenames = filter_files(os.listdir(workdir), extensions)
            lw_files.clear()
            for name in filenames:
                lw_files.addItem(name)

    app = QApplication([])
    win = QWidget()
    win.setWindowTitle('Easy Editor')
    win.resize(700, 500)

    create_widgets()
    layout_widgets()

    workimage = ImageProcessor()

    lw_files.currentRowChanged.connect(workimage.show_chosen_image)
    btn_dir.clicked.connect(show_filenames_list)
    btn_bw.clicked.connect(workimage.do_bw)
    win.show()
    app.exec()


main()
