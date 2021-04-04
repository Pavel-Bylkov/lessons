from random import randint 
import pygame as pg

from constants_globalvars import *

pg.init() 
# во время игры пишем надписи размера 72
font = pg.font.Font(None, 72)

# Запуск игры
pg.display.set_caption("ARCADA") 
window = pg.display.set_mode([win_width, win_height])

back = pg.transform.scale(pg.image.load(img_file_back).convert(), (win_width, win_height)) 

# список всех персонажей игры:
all_sprites = pg.sprite.Group()
# список препятствий:
barriers = pg.sprite.Group()
# список врагов:
enemies = pg.sprite.Group()
# список мин:
bombs = pg.sprite.Group()

# Классы
# класс для цели (стоит и ничего не делает)
class FinalSprite(pg.sprite.Sprite):
  # конструктор класса
  def __init__(self, player_image, x, y, speed):
      # Вызываем конструктор класса (Sprite):
      super().__init__()

      # каждый спрайт должен хранить свойство image - изображение
      self.image = pg.transform.scale(pg.image.load(player_image), (60, 120))
      self.speed = speed

      # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
      
class Hero(pg.sprite.Sprite):
    def __init__(self, filename, x_speed=0, y_speed=0, x=x_start, y=y_start, width=120, height=120):
        pg.sprite.Sprite.__init__(self)
        # создаем свойства, запоминаем переданные значения:
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.direction = 1
        if self.x_speed < 0:
            self.direction = -1
        # картинка загружается из файла и умещается в прямоугольник нужных размеров:
        self.costumes = [pg.transform.scale(pg.image.load(filename), (width, height)).convert_alpha()]
        # добавляем копию отраженную по оси X, картинка смотрит влево
        self.costumes.append(pg.transform.flip(self.costumes[0], True, False))
        self.image =  self.costumes[0] if self.direction > 0 else self.costumes[1]
                    # используем convert_alpha, нам надо сохранять прозрачность

        # каждый спрайт должен хранить свойство rect - прямоугольник. Это свойство нужно для определения касаний спрайтов. 
        self.rect = self.image.get_rect()
        # ставим персонажа в переданную точку (x, y):
        self.rect.x = x 
        self.rect.y = y
        
        # добавим свойство stands_on - это та платформа, на которой стоит персонаж
        self.stands_on = False # если ни на какой не стоит, то значение - False

    def gravitate(self):
        self.y_speed += 0.25

    def jump(self, y):
        if self.stands_on:
            self.y_speed = y

    def update(self):
        ''' перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость'''
        # поворот картинки
        if self.x_speed < 0:
            self.direction = -1
        if self.x_speed > 0:
            self.direction = 1
        self.image =  self.costumes[0] if self.direction > 0 else self.costumes[1]
        # сначала движение по горизонтали
        self.rect.x += self.x_speed
        # если зашли за стенку, то встанем вплотную к стене
        platforms_touched = pg.sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: # идем направо, правый край персонажа - вплотную к левому краю стены
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) # если коснулись сразу нескольких, то правый край - минимальный из возможных
        elif self.x_speed < 0: # идем налево, ставим левый край персонажа вплотную к правому краю стены
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) # если коснулись нескольких стен, то левый край - максимальный

        # теперь движение по вертикали        
        self.gravitate()
        self.rect.y += self.y_speed
        # если зашли за стенку, то встанем вплотную к стене
        platforms_touched = pg.sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: # идем вниз
            for p in platforms_touched:
                self.y_speed = 0 
                # Проверяем, какая из платформ снизу самая высокая, выравниваемся по ней, запоминаем её как свою опору:
                if p.rect.top < self.rect.bottom: 
                    self.rect.bottom = p.rect.top
                    self.stands_on = p
        elif self.y_speed < 0: # идем вверх
            self.stands_on = False # пошли наверх, значит, ни на чем уже не стоим!
            for p in platforms_touched:
                self.y_speed = 0  # при столкновении со стеной вертикальная скорость гасится
                self.rect.top = max(self.rect.top, p.rect.bottom) # выравниваем верхний край по нижним краям стенок, на которые наехали

class Wall(pg.sprite.Sprite):
    def __init__(self, x=20, y=0, width=120, height=120, color=C_GREEN):
        pg.sprite.Sprite.__init__(self)
        # картинка - новый прямоугольник нужных размеров:
        self.image = pg.Surface([width, height])
        self.image.fill(color)

        # создаем свойство rect 
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

class Enemy(pg.sprite.Sprite): # враг
    def __init__(self, x=20, y=0, filename=img_file_enemy, width=100, height=100):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.scale(pg.image.load(filename), (width, height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.side = "left"*randint(0, 1)
        self.left = x - 50
        self.right = x + 50
        self.speed = 2

    def update(self):
        ''' перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость'''
        if self.rect.x <= self.left:
            self.side = "right"
        if self.rect.x >= self.right:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

