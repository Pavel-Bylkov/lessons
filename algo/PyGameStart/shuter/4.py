from pygame import *
from random import randint
from time import time as time_t

# подгружаем отдельно функции для работы со шрифтом
font.init()
font1 = font.Font(None, 100)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

font2 = font.Font(None, 36)

#фоновая музыка
mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.1)
mixer.music.play()
fire_sound = mixer.Sound('laser-blast.ogg')
fire_sound.set_volume(0.3)
bum_sound = mixer.Sound('boom.ogg')
bum_sound.set_volume(0.2)

# нам нужны такие картинки:
img_back = "galaxy.jpg" # фон игры
img_bullet = "bullet.png" # пуля
img_hero = "rocket.png" # герой
img_enemy = "ufo.png" # враг
img_bum = "Взрыв4.png"  # взрыв

# цвета
WHITE_COLOR = (255, 255, 255)

win_width, win_height = 1200, 800
score = 0 # сбито кораблей
goal = 10 # столько кораблей нужно сбить для победы
lost = 0 # пропущено кораблей
max_lost = 3 # проиграли, если пропустили столько

limit_bull = 100  # общее количество пуль
limit_time = 0.4  # время на перезарядку


def text_update(text, num, pos):
    text_img = font2.render(text + str(num), 1, WHITE_COLOR)
    window.blit(text_img, pos)

# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, x, y, size_x, size_y, speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

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
        bullet = Bullet(img_bullet, x=self.rect.centerx, y=self.rect.top, size_x=15, size_y=20, speed=-15)
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
            self.rect.y = randint(-80, - 8) * 10
            lost = lost + 1
 
# класс спрайта-пули   
class Bullet(GameSprite):
    # движение врага
    def update(self):
        self.rect.y += self.speed
        # исчезает, если дойдет до края экрана
        if self.rect.y < 0 or self.rect.y > win_height:
            self.kill()

class Bum(sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        size_x, size_y = 40, 25
        self.bum_img = [transform.scale(image.load(img_bum), (size_x, size_y)),
                        transform.scale(image.load(img_bum), (size_x + 10, size_y + 5)),
                        transform.scale(image.load(img_bum), (size_x + 20, size_y + 10)),
                        transform.scale(image.load(img_bum), (size_x + 30, size_y + 15)),
                        transform.scale(image.load(img_bum), (size_x + 40, size_y + 25)),
                        transform.scale(image.load(img_bum), (size_x + 50, size_y + 35))]
        self.image = self.bum_img[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.i = 1
        self.last_time = time_t()
        bum_sound.play()
    def update(self):
        if self.i < len(self.bum_img) and time_t() - self.last_time > 0.15:
            x, y = self.rect.centerx, self.rect.centery
            self.image = self.bum_img[self.i]
            self.rect = self.image.get_rect()
            self.rect.centerx, self.rect.centery = x, y
            self.i += 1
        elif self.i == len(self.bum_img):
            self.kill()

class Scaner(sprite.Sprite):
    def __init__(self, x) -> None:
        super().__init__()
        self.image = Surface((10,win_height))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = 0

class Boss(GameSprite):
    def __init__(self, boss_image, x, y, size_x, size_y, speed):
        super().__init__(boss_image, x, y, size_x, size_y, speed)
        self.scaner = Scaner(x + size_x//2)
        self.right = win_width - 100
        self.left = 100
        self.direction = "right"*randint(0,1) or "left"
        self.health = 10
        self.last_shot = time_t()
        self.bulletes = sprite.Group()
    def update(self):
        if sprite.collide_rect(self.scaner, ship) and time_t() - self.last_shot > 0.3:
            self.fire()
            self.last_shot = time_t()
        if self.direction == 'left' and self.rect.x <= self.left:
            self.direction = "right"
        elif self.direction == 'right' and self.rect.x >= self.right:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed
        self.scaner.rect.centerx = self.rect.centerx
    # метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def fire(self):
        fire_sound.play()
        bullet = Bullet(img_bullet, x=self.rect.centerx, y=self.rect.bottom, size_x=15, size_y=20, speed=17)
        self.bulletes.add(bullet)

# Создаем окошко
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
 
# создаем спрайты
ship = Player(img_hero, x=5, y=win_height - 100, size_x=80, size_y=100, speed=10)
 
# создание группы спрайтов-врагов
monsters = sprite.Group()
for i in range(1, 6):
    scale = randint(90,200)
    monster = Enemy(img_enemy, x=randint(80, win_width - 80), y=randint(-80, - 8) * 10,
                    size_x=int(50 * scale / 100), size_y=int(30 * scale / 100), speed=randint(1, 5))
    monsters.add(monster)

boss = Boss(img_enemy, x=win_width//2, y=70, size_x=120, size_y=80, speed=12)
bullets = sprite.Group()
bums = sprite.Group()

last_time = time_t() 
# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
final = False
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
        # событие нажатия на пробел - спрайт стреляет
        if e.type == KEYDOWN and e.key == K_SPACE and not finish:
            if limit_bull > 0 and time_t() - last_time > limit_time:
                ship.fire()
                limit_bull -= 1
                last_time = time_t()
 
  # сама игра: действия спрайтов, проверка правил игры, перерисовка
    if not finish:
        # обновляем фон
        window.blit(background,(0,0))

        # пишем текст на экране
        text_update("Счет: ", score, (10, 20))
        text_update("Пропущено: ", lost, (10, 50))
        text_update("Пули: ", limit_bull, (10, 80))

        # производим движения спрайтов
        ship.update()
        bullets.update()
        bums.update()
        if final:
            boss.update()
            boss.reset()
            boss.bulletes.update()
            boss.bulletes.draw(window)
            text_update("Boss: ", boss.health, (win_width - 150, 20))

        monsters.update()
        monsters.draw(window)
        # проверка столкновения пули и монстров (и монстр, и пуля при касании исчезают)
        collides = sprite.groupcollide(monsters, bullets, False, True)
        for c in collides:
            # этот цикл повторится столько раз, сколько монстров подбито
            score = score + 1
            bums.add(Bum(x=c.rect.centerx, y=c.rect.centery))
            if not final:
                c.rect.x = randint(80, win_width - 80)
                c.rect.y = randint(-80, - 8) * 10
                c.speed = randint(1, 5)
            else:
                c.kill()

        # обновляем их в новом местоположении при каждой итерации цикла
        ship.reset()
        bullets.draw(window)
        bums.draw(window)

        if final and boss.health > 0 and sprite.spritecollide(boss, bullets, True):
            boss.health -= 1
            bums.add(Bum(x=boss.rect.centerx, y=boss.rect.bottom))

        # возможный проигрыш: пропустили слишком много или герой столкнулся с врагом
        if (sprite.spritecollide(ship, monsters, False) or lost >= max_lost or
                sprite.spritecollide(ship, boss.bulletes, True)):
            finish = True # проиграли, ставим фон и больше не управляем спрайтами.
            window.blit(lose, (win_width//2 - 150, win_height//2 - 50))

        # проверка выигрыша: сколько очков набрали?
        if score >= goal:
            final = True

        if boss.health <= 0:
            finish = True
            # пишем текст на экране
            window.blit(background,(0,0))
            text_update("Счет: ", score, (10, 20))
            window.blit(win, (win_width//2 - 150,  win_height//2 - 50))

        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)