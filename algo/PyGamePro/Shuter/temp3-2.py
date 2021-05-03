from pygame import (init, sprite, display, time, transform, image, mixer, event, key, font, 
                        QUIT, KEYDOWN, K_SPACE, K_LEFT, K_RIGHT, K_p)
from random import randint
from time import time as time_t
img_back = "galaxy.jpg" # фон игры
img_hero = "rocket.png" # герой
img_enemy = "ufo.png" # враг
img_bullet = "bullet.png"
img_boom = "Взрыв4.png"

sound_fon = "space.ogg"
sound_fire = "laser-blast.ogg"

WHITE = (255, 255, 255)
GREEN = (50, 200, 50)
RED = (200, 50, 50)

score = 0  # сбито кораблей
goal = 15  # столько кораблей нужно сбить для победы
lost = 0  # пропущено кораблей
max_lost = 5  # проиграли, если пропустили столько
life = 3

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
    def fire(self):
        bullet = Bullets(img_bullet, x=self.rect.centerx, y=self.rect.top,
                                        size_x=10, size_y=15, speed=-15)
        bullets.add(bullet)
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

class Bullets(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height or self.rect.y < 0:
            self.kill()

class Boom(sprite.Sprite):
    def __init__(self, x, y, size_x, size_y):
        # Вызываем конструктор класса (Sprite):
        super().__init__()
        size_x //= 2
        size_y //= 2
        self.imgs = [
            transform.scale(image.load(img_boom), (size_x, size_y)),
            transform.scale(image.load(img_boom), (size_x + 10, size_y + 10)),
            transform.scale(image.load(img_boom), (size_x + 20, size_y + 20)),
            transform.scale(image.load(img_boom), (size_x + 30, size_y + 30)),
            transform.scale(image.load(img_boom), (size_x + 40, size_y + 35)),
            transform.scale(image.load(img_boom), (size_x + 50, size_y + 40))
        ]
        self.image = self.imgs[0]
        self.index = 1
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = x, y
        self.last_time = time_t()
    def update(self):
        if self.index < len(self.imgs) and time_t() - self.last_time > 0.1:
            x, y = self.rect.centerx, self.rect.centery
            self.image = self.imgs[self.index]
            self.rect = self.image.get_rect()
            self.rect.centerx, self.rect.centery = x, y
            self.index += 1
            self.last_time = time_t()
        elif self.index == len(self.imgs):
            self.kill()

def text_update(text, num, position):
    window.blit(font2.render(text + str(num), True, WHITE), position)

# Создаем окошко
win_width, win_height = 1200, 800
display.set_caption("Shuter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
init() # Инициализация (настройка) Pygame
font.init()  # Инициализация модуля font
font1 = font.SysFont("Arial", 100)  # Создание объекта Шрифт
font2 = font.SysFont("Arial", 30) 
win = font1.render("YOU WIN!!!", True, GREEN)  # Создание картинки из текста
lose = font1.render("YOU LOSE!!!", True, RED)
pause_img = font1.render("PAUSE", True, WHITE)
# создаем спрайты
ship = Player(img_hero, x=win_width//2, y=win_height - 100,
                            size_x=60, size_y=80, speed=10)
bullets = sprite.Group()
booms = sprite.Group()
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
fire_sound = mixer.Sound(sound_fire)
fire_sound.set_volume(0.3)

finish = False
pause = False
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # перебираем полученные события
    for e in event.get():
        # событие нажатия на крестик окошка
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN and e.key == K_SPACE:
            fire_sound.play()
            ship.fire()
        if e.type == KEYDOWN and e.key == K_p:
            if pause:
                pause = False
            else:
                pause = True
    if not finish and not pause:
        # обновляем фон
        window.blit(background,(0,0))
        # производим движения спрайтов
        ship.update()
        monsters.update()
        bullets.update()
        booms.update()
        # обновляем их в новом местоположении при каждой итерации цикла
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        booms.draw(window)

        text_update(text="Подбито: ", num=score, position=(10, 20))
        text_update(text="Пропущено: ", num=lost, position=(10, 50))
        text_update(text="Жизни: ", num=life, position=(10, 80))

        collides = sprite.groupcollide(monsters, bullets, False, True)
        for c in collides:
            score += 1
            boom = Boom(x=c.rect.centerx, y=c.rect.centery, size_x=c.rect.width, size_y=c.rect.height)
            booms.add(boom)
            c.rect.x = randint(10, win_width - 80)
            c.rect.y = randint(-50, -4)*10
            c.speed = randint(1, 5)
        collides = sprite.spritecollide(ship, monsters, False)
        if life > 0 and collides:
            life -= 1
            for c in collides:
                boom = Boom(x=c.rect.centerx, y=c.rect.centery, size_x=c.rect.width, size_y=c.rect.height)
                booms.add(boom)
                c.rect.x = randint(10, win_width - 80)
                c.rect.y = randint(-50, -4)*10
                c.speed = randint(1, 5)

        if score >= goal:
            finish = True
            final_txt = win
        if lost >= max_lost or life == 0:
            finish = True
            final_txt = lose
    elif not pause:
        window.blit(final_txt, (win_width//2 - 200, win_height//2 - 50))
    else:
       window.blit(pause_img, (win_width//2 - 200, win_height//2 - 50)) 
    display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)
