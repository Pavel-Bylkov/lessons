#подключи нужные модули PIL
from PIL import Image
from PIL import ImageFilter

# класс ImageEditor
class ImageEditor():

    def __init__(self, filename):
        # конструктор класса
        self.filename = filename
        self.original = None
        self.changed = list()
        self.open()

    def open(self):
        # метод "открыть и показать оригинал"
        try:
            self.original = Image.open(self.filename)
            self.original.show()
        except:
            print('Файл не найден!')
            exit()

    def do_left(self):
        # методы для редактирования оригинала
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)

        # бонус. Автоматический нейминг отредатированных картинок
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'

        rotated.save(new_filename)

    # бонус. образать детёныша коалы
    def do_cropped(self):
        box = (250, 100, 600, 400)  # лево, верх, право, низ
        cropped = self.original.crop(box)
        self.changed.append(cropped)

        # бонус. Автоматический нейминг отредатированных картинок
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'

        cropped.save(new_filename)


# создай объект класса ImageEditor с данными картинки-оригинала
MyImage = ImageEditor('original.jpg')

# отредактируй изображение и сохрани результат
MyImage.do_left()
MyImage.do_cropped()

for im in MyImage.changed:
    im.show()
