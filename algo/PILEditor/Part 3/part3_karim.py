import os

from PyQt5.QtCore import Qt # Остановились с Каримом на функции открытия и выбора папки
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Диалог открытия файлов (и папок)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
from PyQt5.QtGui import QPixmap # оптимизированная для показа на экране картинка

from PIL import Image
from PIL import ImageFilter   # BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
                            # EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
                            # GaussianBlur, UnsharpMask

# С какими типами файлов будем работать (растровая графика)
extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
win_weight, win_height = 700, 500


class MainWin(QWidget):
    def __init__(self):
        super().__init__()  # вызываем конструктор родительского класса
        self.resize(win_weight, win_height)
        self.setWindowTitle('Easy Editor')

        self.create_widgets()
        self.layout_widgets()
        self.connects()

    def create_widgets(self):
        """Создаем виджеты для приложения"""
        self.lb_image = QLabel("Картинка")
        self.btn_dir = QPushButton("Выбор папки")
        self.lw_files = QListWidget()

        self.btn_left = QPushButton("Лево")
        self.btn_right = QPushButton("Право")
        self.btn_flip = QPushButton("Зеркало")
        self.btn_sharp = QPushButton("Резкость")
        self.btn_bw = QPushButton("Ч/Б")

    def layout_widgets(self):
        """ Привязка виджетов к линиям и главному окну"""
        row = QHBoxLayout()          # Основная строка
        col1 = QVBoxLayout()         # делится на два столбца
        col2 = QVBoxLayout()

        col1.addWidget(self.btn_dir)      # в первом - кнопка выбора директории
        col1.addWidget(self.lw_files)     # и список файлов

        col2.addWidget(self.lb_image, 95)  # вo втором - картинка

        row_tools = QHBoxLayout()    # и строка кнопок
        row_tools.addWidget(self.btn_left)
        row_tools.addWidget(self.btn_right)
        row_tools.addWidget(self.btn_flip)
        row_tools.addWidget(self.btn_sharp)
        row_tools.addWidget(self.btn_bw)
        col2.addLayout(row_tools)

        row.addLayout(col1, 20)
        row.addLayout(col2, 80)
        self.setLayout(row)

    def connects(self):
        self.btn_dir.clicked.connect(self.showFilenamesList)
        self.lw_files.itemClicked.connect(self.showChosenImage)

    def filter_files(self):
        """Возвращает список отфильтрованных файлов"""
        result = []
        for filename in os.listdir(self.workdir):
            for ext in extensions:
                if filename.endswith(ext):
                    result.append(filename)
        return result

    def showFilenamesList(self):
        """Функция для отображения содержимого выбранной папки"""
        self.workdir = QFileDialog.getExistingDirectory()  # Вызываем диалог для выбора папки
        if self.workdir:
            # получаем список отфильтрованных файлов
            filenames = self.filter_files()
            self.lw_files.clear()
            self.lw_files.addItems(filenames)

    def showChosenImage(self):
        """Функция показывает картинку при выборе файла"""
        if self.lw_files.selectedItems():
            self.filename = self.lw_files.selectedItems()[0].text()
            self.loadImage()
            self.showImage()

    def loadImage(self):
        self.image_path = self.workdir + os.sep + self.filename  # os.path.join(dir, filename)  #
        self.image = Image.open(self.image_path)

    def showImage(self):
        self.lb_image.hide()
        pixmapimage = QPixmap(self.image_path)
        w, h = self.lb_image.width(), self.lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        self.lb_image.setPixmap(pixmapimage)
        self.lb_image.show()


def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec_()

main()