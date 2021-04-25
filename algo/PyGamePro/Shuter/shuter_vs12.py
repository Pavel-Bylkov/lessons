from pygame import * 
from random import randint
from time import time as time_t

def config(): 
    global img_win, img_los, img_back, img_bullet, img_hero, img_enemy, size_x_enemy, size_y_enemy
    global img_bum, win_width, win_height, bull_limit, goal, max_lost, pause_fire
    global sound_fire, sound_bum, sound_fon, FPS
    # нам нужны такие картинки:
    img_win = "thumb.jpg" # фон победы
    img_los = "gameover.png" # фон проигрыша
    img_back = "galaxy.jpg" # фон игры
    
    img_bullet = "камета.png" # пуля
    img_hero = "rocket.png" # герой
    img_enemy = "ufo.png" # враг
    img_bum = "Взрыв4.png" # взрыв
    size_x_enemy, size_y_enemy = 80, 50

    sound_fire = "laser-blast.ogg"
    sound_bum = "bum.ogg"
    sound_fon = "space.ogg"

    win_width = 900
    win_height = 600 
    
    goal = 15 # столько кораблей нужно сбить для победы
    max_lost = 5 # проиграли, если пропустили столько
    pause_fire = 0.2  # Пауза между выстрелами
    bull_limit = 100

    FPS = 15

def vars():
    global score, lost, last_time, finish
    score = 0 # сбито кораблей
    lost = 0 # пропущено кораблей
    last_time = time_t()
    # переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
    finish = False

# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
  def __init__(self, player_image, x, y, size_x, size_y, speed, direction):
      # Вызываем конструктор класса (Sprite):
      #sprite.Sprite.__init__(self)
      super().__init__()
      self.direction = direction
      self.last_time = time_t()
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
    def __init__(self, player_image, x, y, size_x, size_y, speed, direction):
        super().__init__(player_image, x, y, size_x, size_y, speed, direction)
        self.bullets = sprite.Group()
        
    def start(self):
        self.life = 5
        self.hide = False
        self.i = 0
        self.dead = False
        self.limit_bull = bull_limit
        self.rect.x = win_width //2
        self.rect.y = win_height - 100
    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        if not self.hide:
            keys = key.get_pressed()
            if keys[K_LEFT] and self.rect.x > 5:
                self.rect.x -= self.speed
            if keys[K_RIGHT] and self.rect.x < win_width - size_x_sh:
                self.rect.x += self.speed
            if keys[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed // 2
            if keys[K_DOWN] and self.rect.y < win_height - size_y_sh:
                self.rect.y += self.speed
            # событие нажатия на пробел - спрайт стреляет
            if self.limit_bull and keys[K_SPACE] and time_t() - self.last_time > pause_fire:
                self.fire()
                self.limit_bull -= 1
                self.last_time = time_t()
        elif self.i < 10:
            self.i += 1
        else:
            self.dead = True
        self.bullets.update()
    # метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def fire(self):
        fire_sound.play()
        bullet = Bullet(img_bullet, x=self.rect.centerx, y=self.rect.top, size_x=15, size_y=20, speed=15, direction=self.direction)
        self.bullets.add(bullet)
    def reset(self):
        if not self.hide:
            super().reset()
        self.bullets.draw(window)
    def collide(self):
        self.life -= 1
        if self.life == 0:
            self.hide = True
            bum = Bum(self.rect.centerx, self.rect.centery)
            bums.add(bum)
            self.rect.x, self.rect.y = -100, -100

class Enemy_visitor(sprite.Sprite):
    def __init__(self, x) -> None:
        super().__init__()
        self.image = Surface((3,win_height))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0
# класс спрайта-врага   
class Enemy(GameSprite):
    def __init__(self, player_image, x, y, size_x, size_y, speed, direction):
      super().__init__(player_image, x, y, size_x, size_y, speed, direction)
      self.goal = Enemy_visitor(x + size_x // 2)
      self.armor = 3
    # движение врага
    def update(self):
        if (self.armor and sprite.collide_rect(self.goal, ship) 
                and time_t() - self.last_time > pause_fire * 5):
            self.fire()
            self.armor -= 1
            self.last_time = time_t()
        self.rect.y += self.speed
        global lost
        # исчезает, если дойдет до края экрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.goal.rect.x = self.rect.centerx
            self.rect.y = 0
            lost = lost + 1
            self.armor = 3

    def fire(self):
        fire_sound.play()
        bullet = Bullet(img_bullet, x=self.rect.centerx, y=self.rect.bottom,
                    size_x=20, size_y=15, speed=self.speed + 7, direction=self.direction)
        enemy_bullets.add(bullet)
 
# класс спрайта-пули   
class Bullet(GameSprite): 
  # движение врага
  def update(self):
      self.rect.y += self.speed * self.direction
      # исчезает, если дойдет до края экрана
      if self.direction == -1 and self.rect.y < 0:
          self.kill()
      if self.direction == 1 and self.rect.y > win_height:
          self.kill()

class Bum(sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        size_x, size_y = size_x_enemy//2, size_y_enemy//2
        self.bum = [transform.scale(image.load(img_bum), (size_x, size_y)),
            transform.scale(image.load(img_bum), (size_x + 15, size_y + 15)),
            transform.scale(image.load(img_bum), (size_x + 30, size_y + 30)),
            transform.scale(image.load(img_bum), (size_x + 40, size_y + 40)),
            transform.scale(image.load(img_bum), (size_x + 50, size_y + 50))]
        self.i = 1
        self.last_time = time_t()
        self.image = self.bum[0]
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = x, y
    def update(self):
        if self.i < len(self.bum) and time_t() - self.last_time > 0.15:
            x, y = self.rect.centerx, self.rect.centery
            self.image = self.bum[self.i]
            self.rect = self.image.get_rect()
            self.rect.centerx, self.rect.centery = x, y
            self.i += 1
        if self.i == len(self.bum):
            self.kill()

def add_monster():
    size_scale = randint(6, 11)*10
    monster = Enemy(img_enemy, x=randint(80, win_width - 80), y=-40,
            size_x=size_x_enemy*size_scale//100, size_y=size_y_enemy*size_scale//100,
            speed=randint(1, 5), direction=1)
    monsters.add(monster)
def start():
    vars()
    mixer.music.play()
    ship.start()
    for _ in range(6):
        add_monster()

def restart():
    monsters.empty()
    enemy_bullets.empty()
    start()

def text_update(text, num, pos):
    window.blit(font1.render(text + str(num), 1, (255, 255, 255)), pos)

def update():
    # обновляем фон
    window.blit(background,(0,0))

    # пишем текст на экране
    text_update(text="Счет: ", num=score, pos=(10, 20))
    text_update(text="Пропущено: ", num=lost, pos=(10, 50))
    text_update(text="Патроны: ", num=ship.limit_bull, pos=(10, 80))
    text_update(text="Жизни: ", num=ship.life, pos=(10, 110))

    # производим движения спрайтов
    ship.update()
    monsters.update()
    enemy_bullets.update()
    bums.update()
    
    # обновляем их в новом местоположении при каждой итерации цикла
    ship.reset()
    monsters.draw(window)
    enemy_bullets.draw(window)
    bums.draw(window)
# подгружаем отдельно функции для работы со шрифтом
init()
font.init()
# во время игры пишем надписи размера 36
font1 = font.Font(None, 36) 
font2 = font.Font(None, 150)
# Создаем окошко
config() # создаем глобальные переменные
display.set_caption("Шутер")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
win = font2.render("YOU WIN!!", 1, (5, 150, 50))
lose = font2.render("YOU LOSE!!!", 1, (255, 50, 50))
# создаем спрайты
size_x_sh, size_y_sh = 60, 80
ship = Player(img_hero, x=win_width//2, y=win_height - 100,
                size_x=size_x_sh, size_y=size_y_sh, speed=10, direction=-1)
 
# создание группы спрайтов-врагов
monsters = sprite.Group()
enemy_bullets = sprite.Group()

bums = sprite.Group()

# насторойка звуков
mixer.init()
mixer.music.load(sound_fon)
mixer.music.set_volume(0.1)

fire_sound = mixer.Sound(sound_fire)
bum_sound = mixer.Sound(sound_bum)
fire_sound.set_volume(0.3)
bum_sound.set_volume(0.3)

clock = time.Clock()

start()
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
    # сама игра: действия спрайтов, проверка правил игры, перерисовка
    if not finish:
        update()
        # проверка столкновения пули и монстров (и монстр, и пуля при касании исчезают)
        collides = sprite.groupcollide(monsters, ship.bullets, True, True)
        for c in collides:
            bum = Bum(c.rect.centerx, c.rect.centery)
            bums.add(bum)
            bum_sound.play()
            # этот цикл повторится столько раз, сколько монстров подбито
            score = score + 1
            add_monster()
        # проверка столкновения пуль
        sprite.groupcollide(enemy_bullets, ship.bullets, True, True)
        # возможный проигрыш: пропустили слишком много или герой столкнулся с врагом
        if lost >= max_lost or ship.dead:
            finish = True # проиграли, ставим фон и больше не управляем спрайтами.
            final_img = lose
        collide = sprite.spritecollide(ship, monsters, True)
        if (collide or sprite.spritecollide(ship, enemy_bullets, True)):
            for c in collide:
                bum = Bum(c.rect.centerx, c.rect.centery)
                bums.add(bum)
                add_monster()
            ship.collide()
        # проверка выигрыша: сколько очков набрали?
        if score >= goal:
            finish = True
            final_img = win
    else:
        i = 30
        while len(bums) + i > 0:
            update()
            window.blit(final_img, (win_width//2 - 250, win_height//2 - 80))
            display.update()
            clock.tick(FPS)
            i -= 1
        time.delay(3000)
        restart()
    # цикл срабатывает c частотой FPS - кадров в секнуду
    display.update()
    clock.tick(FPS)