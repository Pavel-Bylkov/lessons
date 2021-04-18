from pygame import *
from random import randint
from time import time as time_t
title = "Shuter"
img_back = "galaxy.jpg" # фон игры
img_hero = "rocket.png" # герой
img_enemy = "ufo.png" # враг
img_bullet = "bullet.png"
sound_fon = "space.ogg"
sound_fire = "laser-blast.ogg"

win_width, win_height = 800, 500

N_ENEMY = 7 # количество одновременно атакующих врагов
goal = 15 # столько кораблей нужно сбить для победы
max_lost = 5 # проиграли, если пропустили столько

WHITE_COLOR = (255, 255, 255)

# настройка шрифта
font.init()

# насторойка звуков
mixer.init()
mixer.music.load(sound_fon)
mixer.music.set_volume(0.1)
mixer.music.play()

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
   def reset(self, window):
       window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока
class Player(GameSprite):
    def __init__(self, player_image, x, y, size_x, size_y, speed):
        super().__init__(player_image, x, y, size_x, size_y, speed)
        self.bullets = sprite.Group()
    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullets(img_bullet, x=self.rect.centerx, y=self.rect.top, size_x=10, size_y=15, speed=-15)
        self.bullets.add(bullet)

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
        if self.rect.y < 0 or self.rect.y > win_height:
            self.kill()

# Главный класс игры
class Game():
    def __init__(self) -> None:
        self.create_window()
        self.background = transform.scale(image.load(img_back), (win_width, win_height))
        self.create_sprites()
        self.font = font.Font(None, 36)
        self.fire_sound = mixer.Sound(sound_fire)
        self.fire_sound.set_volume(0.3)
    def create_window(self):
        display.set_caption(title)
        self.window = display.set_mode((win_width, win_height))
    def create_sprites(self):
        # создаем спрайты
        self.ship = Player(img_hero, x=win_width//2, y=win_height - 100,
                                    size_x=60, size_y=80, speed=10)
        # создание группы спрайтов-врагов
        self.monsters = sprite.Group()
        for _ in range(N_ENEMY):
            size_scale = randint(6, 11)*10
            monster = Enemy(img_enemy, x=randint(10, win_width - 80), y=randint(-50, -4)*10,
                            size_x=80*size_scale//100, size_y=50*size_scale//100, speed=randint(1, 5))
            self.monsters.add(monster)
    def start_init(self):
        global score, lost
        score = 0 # сбито кораблей
        lost = 0 # пропущено кораблей
        self.finish = False
        # Основной цикл игры:
        self.run = True # флаг сбрасывается кнопкой закрытия окна  
    def update(self):
        self.ship.update()
        self.ship.bullets.update()
        self.monsters.update()
    def text_update(self, text, num, position):
        text_img = self.font.render(text + str(num), True, WHITE_COLOR)
        self.window.blit(text_img, position)
    def draw(self):
        # обновляем фон
        self.window.blit(self.background,(0,0))
        self.text_update("Счет: ", score, (10, 20))
        self.text_update("Пропущено: ", lost, (10, 50))
        # обновляем их в новом местоположении при каждой итерации цикла
        self.ship.reset(self.window)
        self.monsters.draw(self.window)
        self.ship.bullets.draw(self.window)
    def collides(self):
        global score
        collides = sprite.groupcollide(self.monsters, self.ship.bullets, False, True)
        for c in collides:
            score += 1
            c.rect.x = randint(10, win_width - 80)
            c.rect.y = randint(-50, -4)*10
            c.speed = randint(1, 5)
        self.ship_collide = sprite.spritecollide(self.ship, self.monsters, False)

    def check_finish(self):
        pass
    def game_loop(self):
        self.start_init()
        while self.run:
            # перебираем полученные события
            for e in event.get():
                # событие нажатия на крестик окошка
                if e.type == QUIT:
                    self.run = False
                if e.type == KEYDOWN and e.key == K_SPACE:
                    self.fire_sound.play()
                    self.ship.fire()
            if not self.finish:
                # производим движения спрайтов
                self.update()
                # отрисовка фона и спрайтов на экранной поверхности
                self.draw()
                # проверяем столкновения спрайтов
                self.collides()
                # проверка условий победы и поражения
                self.check_finish()
                display.update()
            # цикл срабатывает каждую 0.05 секунд
            time.delay(50)

game = Game()
game.game_loop()