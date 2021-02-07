import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QFileDialog, # Диалог открытия файлов (и папок)
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)

from PyQt5.QtCore import Qt # нужна константа Qt.KeepAspectRatio для изменения размеров с сохранением пропорций
from PyQt5.QtGui import QPixmap # оптимизированная для показа на экране картинка

from PIL import Image

########### Занятие 1. Создание объектов интерфейса: #########
app = QApplication([])
win = QWidget()        
win.resize(700, 500)  
win.setWindowTitle('Easy Editor')
lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()

btn_left = QPushButton("Лево")
btn_right = QPushButton("Право")
btn_flip = QPushButton("Зеркало")
btn_sharp = QPushButton("Резкость")
btn_bw = QPushButton("Ч/Б")

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

win.show()

########### Занятие 1. Чтение и отображение имён файлов папки #########

workdir = ''

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
    extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)

    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)

btn_dir.clicked.connect(showFilenamesList)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"

    def loadImage(self, dir, filename):
        ''' при загрузке запоминаем путь и имя файла '''
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def showImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

workimage = ImageProcessor()

def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)

lw_files.currentRowChanged.connect(showChosenImage)


app.exec()