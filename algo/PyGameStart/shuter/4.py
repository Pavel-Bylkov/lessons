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

# нам нужны такие картинки:
img_back = "galaxy.jpg" # фон игры
img_bullet = "bullet.png" # пуля
img_hero = "rocket.png" # герой
img_enemy = "ufo.png" # враг
img_bum = "Взрыв4.png"  # взрыв

# цвета
WHITE_COLOR = (255, 255, 255)

score = 0 # сбито кораблей
goal = 10 # столько кораблей нужно сбить для победы
lost = 0 # пропущено кораблей
max_lost = 3 # проиграли, если пропустили столько

limit_bull = 100  # общее количество пуль
limit_time = 0.5  # время на перезарядку


def text_update(text, num):
    return font2.render(text + str(num), 1, WHITE_COLOR)

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
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
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
    # движение врага
    def update(self):
        self.rect.y += self.speed
        # исчезает, если дойдет до края экрана
        if self.rect.y < 0:
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
    def update(self):
        if self.i < len(self.bum_img) and time_t() - self.last_time > 0.15:
            x, y = self.rect.centerx, self.rect.centery
            self.image = self.bum_img[self.i]
            self.rect = self.image.get_rect()
            self.rect.centerx, self.rect.centery = x, y
            self.i += 1
        elif self.i == len(self.bum_img):
            self.kill()

# Создаем окошко
win_width = 1400
win_height = 800
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
 
# создаем спрайты
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
 
# создание группы спрайтов-врагов
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)
 
bullets = sprite.Group()
bums = sprite.Group()

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
        window.blit(text_update("Счет: ", score), (10, 20))
        window.blit(text_update("Пропущено: ", lost), (10, 50))
        window.blit(text_update("Пули: ", limit_bull), (10, 80))

        # производим движения спрайтов
        ship.update()
        monsters.update()
        bullets.update()
        bums.update()

        # обновляем их в новом местоположении при каждой итерации цикла
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        bums.draw(window)
 
        # проверка столкновения пули и монстров (и монстр, и пуля при касании исчезают)
        collides = sprite.groupcollide(monsters, bullets, False, True)
        for c in collides:
            # этот цикл повторится столько раз, сколько монстров подбито
            score = score + 1
            bums.add(Bum(x=c.rect.centerx, y=c.rect.centery))
            c.rect.x = randint(80, win_width - 80)
            c.rect.y = -40
            c.speed = randint(1, 5)

        # возможный проигрыш: пропустили слишком много или герой столкнулся с врагом
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True # проиграли, ставим фон и больше не управляем спрайтами.
            window.blit(lose, (win_width//2 - 150, win_height//2 - 50))

        # проверка выигрыша: сколько очков набрали?
        if score >= goal:
            finish = True
            # пишем текст на экране
            display.update()
            window.blit(background,(0,0))
            text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
            window.blit(text, (10, 20))
            window.blit(win, (win_width//2 - 150,  win_height//2 - 50))

        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)