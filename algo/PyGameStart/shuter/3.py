from pygame import *
from random import randint
from time import time as time_t
#фоновая музыка
mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.1)
mixer.music.play()
fire_sound = mixer.Sound('laser-blast.ogg')
fire_sound.set_volume(0.3)
boom_sound = mixer.Sound('boom.ogg')
boom_sound.set_volume(0.2)

# цвета
WHITE_COLOR = (255, 255, 255)
RED_COLOR = (180, 0, 0)
GREEN_COLOR = (0, 180, 0)

#шрифты и надписи
font.init()
font1 = font.Font(None, 150)
win = font1.render('YOU WIN!', True, GREEN_COLOR)
lose = font1.render('YOU LOSE!', True, RED_COLOR)
font2 = font.Font(None, 36)

# нам нужны такие картинки:
img_back = "galaxy.jpg" # фон игры
img_hero = "rocket.png" # герой
img_enemy = "ufo.png" # враг
img_bull = "blaster.png"  # пуля
img_boom = "Взрыв4.png" # взрыв

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
        bullet = Bullet(img_bull, x=self.rect.centerx-15, y=self.rect.top,
                                size_x=30, size_y=40, speed=-15)
        self.bullets.add(bullet)

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
        if self.rect.y < 0:
            self.kill()

class Boom(sprite.Sprite):
    def __init__(self, x, y, size_x, size_y) -> None:
        super().__init__()
        size_x //= 2
        size_y //= 2
        self.boom_imgs = [
            transform.scale(image.load(img_boom), (size_x, size_y)),
            transform.scale(image.load(img_boom), (size_x + 5, size_y + 5)),
            transform.scale(image.load(img_boom), (size_x + 15, size_y + 10)),
            transform.scale(image.load(img_boom), (size_x + 25, size_y + 20)),
            transform.scale(image.load(img_boom), (size_x + 35, size_y + 25)),
            transform.scale(image.load(img_boom), (size_x + 40, size_y + 30))
        ]
        self.image = self.boom_imgs[0]
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = x, y
        self.i = 1
        self.last_time = time_t()
        boom_sound.play()
    def update(self):
        if self.i < len(self.boom_imgs) and time_t() - self.last_time > 0.25:
            x, y = self.rect.centerx, self.rect.centery
            self.image = self.boom_imgs[self.i]
            self.rect = self.image.get_rect()
            self.rect.centerx, self.rect.centery = x, y
            self.i += 1
        elif self.i == len(self.boom_imgs):
            self.kill()

def text_update(text, num, pos):
    window.blit(font2.render(text + str(num), 1, WHITE_COLOR), pos)

def monsters_collide_actions(collides, score):
    for c in collides:
        # этот цикл повторится столько раз, сколько монстров подбито
        score = score + 1
        boom = Boom(x=c.rect.centerx, y=c.rect.centery, size_x=c.rect.width, size_y=c.rect.height)
        booms.add(boom)
        c.rect.x = randint(80, win_width - 80)
        c.rect.y = randint(-80, - 8) * 10
        c.speed = randint(1, 5)
    return score

def main_update():
    window.blit(background,(0,0))
    monsters.update()
    ship.bullets.update()
    booms.update()
    monsters.draw(window)
    ship.bullets.draw(window)
    booms.draw(window)
    text_update("Счет: ", score, (10, 20))
    text_update("Пропущено: ", lost, (10, 50))
    text_update("Патроны: ", limit_bull, (10, 80))
    
def start_game():
    global score, lost, goal, max_lost, limit_bull, limit_time, finish
    score = 0 # сбито кораблей
    lost = 0 # пропущено кораблей
    goal = 10 # цель
    max_lost = 3 # проиграли, если пропустили столько

    limit_bull = 100  # общее количество пуль
    limit_time = 0.3  # время на перезарядку
    # переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
    finish = False
    ship.rect.centerx = win_width//2
    for i in range(1, 6):
        scale = randint(90,200)
        monster = Enemy(img_enemy, x=randint(80, win_width - 80), y=randint(-80, - 8) * 10,
                        size_x=int(50 * scale / 100), size_y=int(30 * scale / 100), speed=randint(1, 5))
        monsters.add(monster)
# Создаем окошко
win_width = 1200
win_height = 800
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# создаем спрайты
size_x, size_y = 80, 100
ship = Player(img_hero, x=win_width//2, y=win_height - size_y, size_x=size_x, size_y=size_y, speed=10)
ship.bullets = sprite.Group()
monsters = sprite.Group()
booms = sprite.Group()

start_game()

last_time = time_t()
clock = time.Clock()
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
        # событие нажатия на пробел - спрайт стреляет
        if e.type == KEYDOWN and e.key == K_SPACE:
            if limit_bull > 0 and time_t() - last_time > limit_time:
                ship.fire()
                limit_bull -= 1
                last_time = time_t()

    if not finish:
        main_update()

        # производим движения спрайтов
        ship.update()
        ship.reset()

        collides = sprite.groupcollide(monsters, ship.bullets, False, True)
        score = monsters_collide_actions(collides, score)

        if score >= goal:
            finish = True
            final_text = win
              
        collides = sprite.spritecollide(ship, monsters, False)
        if lost >= max_lost or collides:
            boom = Boom(x=ship.rect.centerx, y=ship.rect.centery,
                            size_x=ship.rect.width, size_y=ship.rect.height)
            booms.add(boom)
            monsters_collide_actions(collides, 0)
            finish = True
            final_text =lose

        display.update()
    else:
        while len(booms):
            main_update()
            window.blit(final_text, (win_width//2 - 200,  win_height//2 - 80))
            display.update()
            clock.tick(30)  
        for  _ in range(30):
            window.blit(final_text, (win_width//2 - 200,  win_height//2 - 80))
            display.update()
            clock.tick(30)     
        for b in ship.bullets:
            b.kill()
        for m in monsters:
            m.kill()
        time.delay(3000)
        start_game()

    # цикл срабатывает каждую 0.05 секунд
    #time.delay(50)
    clock.tick(30)