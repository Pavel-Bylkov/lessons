import os
from pygame import *
from random import randint
from time import time as time_t

#фоновая музыка
mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.1)
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
fire_sound.set_volume(0.3)

#шрифты и надписи
font.init()
font2 = font.Font(None, 36)

# цвета
WHITE_COLOR = (255, 255, 255)

# нам нужны такие картинки:
img_back = "galaxy.jpg" # фон игры
img_hero = "rocket.png" # герой
img_enemy = "ufo.png" # враг
img_bull = "bullet.png"  # пуля

score = 0 # сбито кораблей
lost = 0 # пропущено кораблей

limit_bull = 100  # общее количество пуль
limit_time = 0.5  # время на перезарядку

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
    # метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def fire(self):
        fire_sound.play()
        bullet = Bullet(img_bull, x=self.rect.centerx, y=self.rect.top,
                                size_x=15, size_y=20, speed=15)
        bullets.add(bullet)

# класс спрайта-врага   
class Enemy(GameSprite):
    # движение врага
    def update(self):
        self.rect.y += self.speed
        global lost
        # исчезает, если дойдет до края экрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

# класс спрайта-пули   
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        # исчезает, если дойдет до края экрана
        if self.rect.y < 0:
            self.kill()

os.environ['SDL_VIDEO_CENTERED'] = '1'
init()
# Создаем окошко
win_width = 1200
win_height = 800
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# создаем спрайты
ship = Player(img_hero, x=5, y=win_height - 100, size_x=80, size_y=100, speed=10)
bullets = sprite.Group()
monsters = sprite.Group()
for i in range(1, 8):
    monster = Enemy(img_enemy, x=randint(80, win_width - 80), y=-40,
                            size_x=80, size_y=50, speed=randint(1, 5))
    monsters.add(monster)

last_time = time_t()
# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN and e.key == K_SPACE:
            if limit_bull > 0 and time_t() - last_time > limit_time:
                ship.fire()
                limit_bull -= 1
                last_time = time_t()

    if not finish:
        # обновляем фон
        window.blit(background,(0,0))
        # пишем текст на экране
        text = font2.render("Счет: " + str(score), 1, WHITE_COLOR)
        window.blit(text, (10, 20))
        text_lose = font2.render("Пропущено: " + str(lost), 1, WHITE_COLOR)
        window.blit(text_lose, (10, 50))
        # производим движения спрайтов
        ship.update()
        bullets.update()
        monsters.update()
        # обновляем их в новом местоположении при каждой итерации цикла
        ship.reset()
        bullets.draw(window)
        monsters.draw(window)

        # проверка столкновения пули и монстров (и монстр, и пуля при касании исчезают)
        collides = sprite.groupcollide(monsters, bullets, False, True)
        for c in collides:
            # этот цикл повторится столько раз, сколько монстров подбито
            score = score + 1
            c.rect.x = randint(80, win_width - 80)
            c.rect.y = -40
            c.speed = randint(1, 5)

        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)