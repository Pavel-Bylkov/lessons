import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit, QListWidget,
                                QGroupBox, QRadioButton, QPushButton, QLabel, 
                                QHBoxLayout, QPushButton, QInputDialog, QFileDialog)
from PyQt5.QtGui import QPixmap # оптимизированная для показа на экране картинка
from PIL import Image

win_title = "Easy Editor"
win_size = 700, 500
extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

class MainWin(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(win_title)
        self.resize(*win_size)
        self.save_dir = "Modified"

        self.create_widgets()
        self.layout_widgets()

        self.connects()

    def create_widgets(self):
        """Создаем виджеты для приложения"""
        self.lb_image = QLabel("Здесь будет картинка")
        self.btn_dir = QPushButton("Папка")
        self.lw_files = QListWidget()

        self.btn_left = QPushButton("Лево")
        self.btn_right = QPushButton("Право")
        self.btn_flip = QPushButton("Зеркало")
        self.btn_sharp = QPushButton("Резкость")
        self.btn_bw = QPushButton("Ч/б")

    def layout_widgets(self):
        """ Привязка виджетов к линиям и главному окну"""
        row = QHBoxLayout()
        col1 = QVBoxLayout()
        col2 = QVBoxLayout()
        col1.addWidget(self.btn_dir)
        col1.addWidget(self.lw_files)

        col2.addWidget(self.lb_image, 95)

        row_tools = QHBoxLayout()
        row_tools.addWidget(self.btn_left)
        row_tools.addWidget(self.btn_right)
        row_tools.addWidget(self.btn_flip)
        row_tools.addWidget(self.btn_sharp)
        row_tools.addWidget(self.btn_bw)
        col2.addLayout(row_tools)

        row.addLayout(col1, 20)
        row.addLayout(col2, 80)
        self.setLayout(row)

    def chooseWorkdir(self):
        """Функция выбора рабочей папки"""
        self.workdir = QFileDialog.getExistingDirectory()

    def filter(self):
        """Функция отбора имён файлов по расширениям"""
        self.filenames = []
        for filename in os.listdir(self.workdir):
            for ext in extensions:
                if filename.lower().endswith(ext):
                    self.filenames.append(filename)

    def showFilenamesList(self):
        """Функция-обработчик нажатия на кнопку «Папка»"""
        self.chooseWorkdir()
        if self.workdir:
            self.filter()
            self.lw_files.clear()
            self.lw_files.addItems(sorted(self.filenames))

    def loadImage(self):
        """Метод открывает файл и создает объект Image"""
        self.image_path = os.path.join(self.workdir, self.filename)
        self.image = Image.open(self.image_path)

    def showImage(self):
        self.lb_image.hide()
        pixmapimage = QPixmap(self.image_path)
        w, h = self.lb_image.width(), self.lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        self.lb_image.setPixmap(pixmapimage)
        self.lb_image.show()

    def showChosenImage(self):
        """Функция показывает картинку при выборе файла"""
        if self.lw_files.selectedItems():
            self.filename = self.lw_files.selectedItems()[0].text()
            self.loadImage()
            self.showImage()

    def createModified(self):
        path = os.path.join(self.workdir, self.save_dir)
        if not (os.path.exists(path) and os.path.isdir(path)):
            os.mkdir(path)

    def saveImage(self):
        """сохраняет копию файла в подпапке  Modified"""
        self.createModified()
        new_image_path = os.path.join(self.workdir, self.save_dir, self.filename)
        self.image.save(new_image_path)

    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        self.image_path = os.path.join(self.workdir, self.save_dir, self.filename)
        self.showImage()

    def connects(self):
        """Метод для привязки событий к обработчикам"""
        self.btn_dir.clicked.connect(self.showFilenamesList)
        self.lw_files.itemClicked.connect(self.showChosenImage)
        self.btn_bw.clicked.connect(self.do_bw)

    
def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec_()

main()