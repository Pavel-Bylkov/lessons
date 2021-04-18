from pygame import *
from random import randint
from time import time as time_t
img_back = "galaxy.jpg" # фон игры
img_hero = "rocket.png" # герой
img_enemy = "ufo.png" # враг

sound_fon = "space.ogg"

score = 0 # сбито кораблей
goal = 15 # столько кораблей нужно сбить для победы
lost = 0 # пропущено кораблей
max_lost = 5 # проиграли, если пропустили столько

# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
   # конструктор класса
   def __init__(self, player_image, x, y, size_x, size_y, speed):
       # Вызываем конструктор класса (Sprite):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y

   # метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока
class Player(GameSprite):
   # метод для управления спрайтом стрелками клавиатуры
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed

# класс спрайта-врага   
class Enemy(GameSprite):
    # движение врага
    def update(self):
        self.rect.y += self.speed
        global lost
        # исчезает, если дойдет до края экрана
        if self.rect.y > win_height:
            self.rect.x = randint(10, win_width - 80)
            self.rect.y = randint(-10, -2)*10
            lost = lost + 1
# Создаем окошко
win_width, win_height = 800, 500
display.set_caption("Shuter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
# создаем спрайты
ship = Player(img_hero, x=win_width//2, y=win_height - 100,
                            size_x=60, size_y=80, speed=10)
# создание группы спрайтов-врагов
monsters = sprite.Group()
for _ in range(6):
    size_scale = randint(6, 11)*10
    monster = Enemy(img_enemy, x=randint(10, win_width - 80), y=randint(-50, -4)*10,
                    size_x=80*size_scale//100, size_y=50*size_scale//100, speed=randint(1, 5))
    monsters.add(monster)

# насторойка звуков
mixer.init()
mixer.music.load(sound_fon)
mixer.music.set_volume(0.1)
mixer.music.play()

finish = False
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # перебираем полученные события
    for e in event.get():
        # событие нажатия на крестик окошка
        if e.type == QUIT:
            run = False
    if not finish:
        # обновляем фон
        window.blit(background,(0,0))
        # производим движения спрайтов
        ship.update()
        monsters.update()
        # обновляем их в новом местоположении при каждой итерации цикла
        ship.reset()
        monsters.draw(window)

        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)
