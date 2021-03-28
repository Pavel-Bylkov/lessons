from random import randint 
import pygame

from constants_globalvars import *

# Классы
# класс для цели (стоит и ничего не делает)
class FinalSprite(pygame.sprite.Sprite):
  # конструктор класса
  def __init__(self, player_image, player_x, player_y, player_speed):
      # Вызываем конструктор класса (Sprite):
      pygame.sprite.Sprite.__init__(self)

      # каждый спрайт должен хранить свойство image - изображение
      self.image = pygame.transform.scale(pygame.image.load(player_image), (60, 120))
      self.speed = player_speed

      # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
      
class Hero(pygame.sprite.Sprite):
    def __init__(self, filename, x_speed=0, y_speed=0, x=x_start, y=y_start, width=120, height=120):
        pygame.sprite.Sprite.__init__(self)
        # картинка загружается из файла и умещается в прямоугольник нужных размеров:
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)).convert_alpha() 
                    # используем convert_alpha, нам надо сохранять прозрачность

        # каждый спрайт должен хранить свойство rect - прямоугольник. Это свойство нужно для определения касаний спрайтов. 
        self.rect = self.image.get_rect()
        # ставим персонажа в переданную точку (x, y):
        self.rect.x = x 
        self.rect.y = y
        # создаем свойства, запоминаем переданные значения:
        self.x_speed = x_speed
        self.y_speed = y_speed
        # добавим свойство stands_on - это та платформа, на которой стоит персонаж
        self.stands_on = False # если ни на какой не стоит, то значение - False

    def gravitate(self):
        self.y_speed += 0.25

    def jump(self, y):
        if self.stands_on:
            self.y_speed = y

    def update(self):
        ''' перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость'''
        # сначала движение по горизонтали
        self.rect.x += self.x_speed
        # если зашли за стенку, то встанем вплотную к стене
        platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
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
        platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
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

class Wall(pygame.sprite.Sprite):
    def __init__(self, x=20, y=0, width=120, height=120, color=C_GREEN):
        pygame.sprite.Sprite.__init__(self)
        # картинка - новый прямоугольник нужных размеров:
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # создаем свойство rect 
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

class Enemy(pygame.sprite.Sprite): # враг
    def __init__(self, x=20, y=0, filename=img_file_enemy, width=100, height=100):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

    def update(self):
        ''' перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость'''
        self.rect.x += randint(-5, 5)
        self.rect.y += randint(-5, 5)