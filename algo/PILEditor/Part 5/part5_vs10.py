import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QListWidget,
                             QHBoxLayout, QVBoxLayout, QFileDialog)
from PyQt5.QtGui import QPixmap  # оптимизированная для показа на экране картинка
from PIL import Image
from PIL import ImageFilter     #  BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
                                # EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
                                # GaussianBlur, UnsharpMask


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
        self.show_image()

    def save_image(self):
        """сохраняет копию файла в подпапке"""
        path = os.path.join(workdir, self.save_dir)
        if not (os.path.exists(path) and os.path.isdir(path)):
            os.mkdir(path)
        self.image_path = os.path.join(path, self.filename)
        self.image.save(self.image_path)

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        self.show_image()
    
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        self.show_image()

    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        self.show_image()

    def do_sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.save_image()
        self.show_image()
    
    def do_zoom(self):
        top, bottom = int(self.image.size[1] * 0.2), int(self.image.size[1] * 0.8)
        left, right = int(self.image.size[0] * 0.2), int(self.image.size[0] * 0.8)
        box = (left, top, right, bottom)  # лево, верх, право, низ
        self.image = self.image.crop(box)
        self.save_image()
        self.show_image()

def main():
    def create_widgets():
        """Создаем виджеты для приложения"""
        global lb_image, btn_dir, lw_files, btn_left, btn_right, btn_flip, btn_sharp, btn_bw, btn_zoom
        lb_image = QLabel("Здесь будет картинка")
        btn_dir = QPushButton("Папка")
        lw_files = QListWidget()

        btn_left = QPushButton("Лево")
        btn_right = QPushButton("Право")
        btn_flip = QPushButton("Зеркало")
        btn_sharp = QPushButton("Резкость")
        btn_bw = QPushButton("Ч/Б")
        btn_zoom = QPushButton("Zoom")

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
        row_tools.addWidget(btn_zoom)
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

    def filter_files(extensions):
        """Функция отбора имён файлов по расширениям"""
        result = []
        for filename in os.listdir(workdir):
            for ext in extensions:
                if filename.endswith(ext):
                    result.append(filename)
        return result

    def show_filenames_list():
        """Функция-обработчик нажатия на кнопку «Папка».
            Отвечает за выбор папки, отбор файлов и отображение их в виджете."""
        extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
        if chooseWorkdir():
            filenames = filter_files(extensions)
            lw_files.clear()
            lw_files.addItems(filenames)

    app = QApplication([])
    win = QWidget()
    win.setWindowTitle('Easy Editor')
    win.resize(700, 500)

    create_widgets()
    layout_widgets()

    workimage = ImageProcessor()

    def connects():
        lw_files.currentRowChanged.connect(workimage.show_chosen_image)
        btn_dir.clicked.connect(show_filenames_list)
        btn_bw.clicked.connect(workimage.do_bw)
        btn_flip.clicked.connect(workimage.do_flip)
        btn_left.clicked.connect(workimage.do_left)
        btn_right.clicked.connect(workimage.do_right)
        btn_sharp.clicked.connect(workimage.do_sharpen)
        btn_zoom.clicked.connect(workimage.do_zoom)
    connects()

    win.show()
    app.exec()


main()
