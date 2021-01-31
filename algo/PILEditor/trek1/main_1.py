from PIL import Image
from PIL import ImageFilter

#для бонусной задачи
from PIL import ImageEnhance

#открой файл с оригиналом картинки
with Image.open('original.jpg') as pic_original:
    print('Изображение открыто\nРазмер:', pic_original.size[0], "x", pic_original.size[1])
    print('Формат:', pic_original.format)
    print('Тип:', pic_original.mode) #цветное
    pic_original.show()

    # сделай оригинал изображения чёрно-белым
    pic_gray = pic_original.convert('L')
    pic_gray.save('gray.jpg')
    print('Изображение создано\nРазмер:', pic_gray.size[0], "x", pic_gray.size[1])
    print('Формат:', pic_gray.format)
    print('Тип:', pic_gray.mode) #чб
    pic_gray.show()

    # сделай оригинал изображения размытым
    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save('blured.jpg')
    pic_blured.show()

    # поверни оригинал изображения на 180 градусов
    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.save('up.jpg')
    pic_up.show()


    #бонус 1. Зеркальное отражение.
    pic_mirrow = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_mirrow.save('mirrow.jpg')
    pic_mirrow.show()

    #бонус 2. Увеличение контраста.
    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.save('contr.jpg')
    pic_contrast.show()

with Image.open('gray.jpg') as pic_original:
    print('Изображение открыто\nРазмер:', pic_original.size[0], "x", pic_original.size[1])
    print('Формат:', pic_original.format)
    print('Тип:', pic_original.mode) #цветное
    pic_original.show()