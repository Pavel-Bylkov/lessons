from pygame import init, display, sprite, font, time, image, transform, mixer, event, key, Surface
from pygame import K_LEFT, K_RIGHT, QUIT, KEYDOWN, K_SPACE
from random import randint
from time import time as time_t #импортируем функцию для засекания времени, 
                                # чтобы интерпретатор не искал эту функцию в pygame модуле time, 
                                # даём ей другое название сами

init() # инициализация pygame
def consts():
    global font2, win, lose, fire_sound, boom_sound, win_width, win_height, title
    global img_back, img_bullet, img_hero, img_enemy, img_ast, img_boom
    global WHITE_COLOR, GREEN_COLOR, ORANGE_COLOR, RED_COLOR
    # цвета
    WHITE_COLOR = (255, 255, 255)
    GREEN_COLOR = (0, 150, 0)
    ORANGE_COLOR = (150, 150, 0)
    RED_COLOR = (150, 0, 0)
    #подгружаем отдельно функции для работы со шрифтом
    font.init()
    font1 = font.Font(None, 150)
    win = font1.render('YOU WIN!', True,  WHITE_COLOR)
    lose = font1.render('YOU LOSE!', True, RED_COLOR)
    
    font2 = font.Font(None, 36)
    
    #фоновая музыка
    mixer.init()
    mixer.music.load('space.ogg')
    mixer.music.set_volume(0.1)
    fire_sound = mixer.Sound('laser-blast.ogg')
    fire_sound.set_volume(0.3)
    boom_sound = mixer.Sound('boom.ogg')
    boom_sound.set_volume(0.2)

    #нам нужны такие картинки:
    img_back = "galaxy.jpg" #фон игры
    img_bullet = "bullet.png" #пуля
    img_hero = "rocket.png" #герой
    img_enemy = "ufo.png" #враг
    img_ast = "asteroid.png" #астероид
    img_boom = "Взрыв4.png"  # взрыв

    # параметры окна
    win_width, win_height = 1200, 800
    title = "Shooter"

def vars():
    global score, goal, lost, max_lost, life, limit_bull, limit_time, finish, final
    score = 0 #сбито кораблей
    goal = 20 #столько кораблей нужно сбить для победы
    lost = 0 #пропущено кораблей
    max_lost = 10 #проиграли, если пропустили столько кораблей
    life = 3  #очки жизни

    limit_bull = 100  # общее количество пуль
    limit_time = 0.4  # время на перезарядку
    
    # переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
    finish = False
    final = False

#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
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
    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
  #метод для управления спрайтом стрелками клавиатуры
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
 
   #метод "выстрел" (используем место игрока, чтобы создать там пулю)
   def fire(self):
        bullet = Bullet(img_bullet, x=self.rect.centerx, y=self.rect.top, size_x=15, size_y=20, speed=-15)
        self.bullets.add(bullet)
#класс спрайта-врага 
class Enemy(GameSprite):
  #движение врага
  def update(self):
      self.rect.y += self.speed
      global lost
      #исчезает, если дойдёт до края экрана
      if self.rect.y > win_height:
          self.rect.x = randint(80, win_width - 80)
          self.rect.y = randint(-80, - 8) * 10
          lost = lost + 1
class Asteroid(GameSprite):
  #движение врага
  def update(self):
      self.rect.y += self.speed
      #исчезает, если дойдёт до края экрана
      if self.rect.y > win_height:
          self.rect.x = randint(80, win_width - 80)
          self.rect.y = randint(-80, - 8) * 10
#класс спрайта-пули 
class Bullet(GameSprite):
  #движение врага
  def update(self):
      self.rect.y += self.speed
      #исчезает, если дойдёт до края экрана
      if self.rect.y < 0 or self.rect.y > win_height:
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
        if self.i < len(self.boom_imgs) and time_t() - self.last_time > 0.2:
            x, y = self.rect.centerx, self.rect.centery
            self.image = self.boom_imgs[self.i]
            self.rect = self.image.get_rect()
            self.rect.centerx, self.rect.centery = x, y
            self.i += 1
        elif self.i == len(self.boom_imgs):
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

def text_update(text, num, pos):
    #задаём разный цвет в зависимости от количества жизней
    color = WHITE_COLOR
    if text == "Жизни: ":
        if life == 3:
            color = GREEN_COLOR
        elif life == 2:
            color = ORANGE_COLOR
        else:
            color = RED_COLOR
    window.blit(font2.render(text + str(num), 1, color), pos)

def monsters_collide_actions(collides, score):
    for c in collides:
        # этот цикл повторится столько раз, сколько монстров подбито
        score = score + 1
        boom_monster(c, x=c.rect.centerx, y=c.rect.centery, size_x=c.rect.width, size_y=c.rect.height)
    return score

def ship_collides_actions(enemies, boom):
    global life
    collides = sprite.spritecollide(ship, enemies, False)
    if boom and collides:
        for enemy in collides:
            boom_monster(enemy, x=enemy.rect.centerx, y=enemy.rect.centery, size_x=enemy.rect.width, size_y=enemy.rect.height)
        life = life -1
    elif collides:
        life = life -1
    if life == 0:
        boom = Boom(x=ship.rect.centerx, y=ship.rect.centery, size_x=ship.rect.width, size_y=ship.rect.height)
        booms.add(boom)

def boom_monster(monster, x, y, size_x, size_y):
    boom = Boom(x, y, size_x, size_y)
    booms.add(boom)
    monster.rect.x = randint(80, win_width - 80)
    monster.rect.y = randint(-80, - 8) * 10
    monster.speed = randint(1, 5)

def main_update():
    window.blit(background,(0,0))
    text_update("Счет: ", score, (10, 20))
    text_update("Пропущено: ", lost, (10, 50))
    text_update("Патроны: ", limit_bull, (10, 80))
    text_update("Жизни: ", life, (10, 110))
    monsters.update()
    asteroids.update()
    ship.bullets.update()
    booms.update()
    monsters.draw(window)
    asteroids.draw(window)
    ship.bullets.draw(window)
    booms.draw(window)
    if final:
        boss.update()
        boss.reset()
        boss.bulletes.update()
        boss.bulletes.draw(window)
        text_update("Boss: ", boss.health, (win_width - 150, 20))
            #производим движения спрайтов
    if life > 0:
        ship.update()

        #обновляем их в новом местоположении при каждой итерации цикла
        ship.reset()

def start_game():
    vars()  # присваиваем стартовые значения переменным
    ship.rect.centerx = win_width//2
    for i in range(1, 6):
        scale = randint(90,200)
        monster = Enemy(img_enemy, x=randint(80, win_width - 80), y=randint(-80, - 8) * 10,
                        size_x=int(50 * scale / 100), size_y=int(30 * scale / 100), speed=randint(1, 5))
        monsters.add(monster)
    for i in range(1, 3):
        asteroid = Asteroid(img_ast, randint(30, win_width - 30), -40, 80, 50, randint(1, 7))
        asteroids.add(asteroid)
    mixer.music.play()

consts()
#создаём окошко
display.set_caption(title)
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
#создаём спрайты
ship = Player(img_hero, x=5, y=win_height - 100, size_x=80, size_y=100, speed=10)
ship.bullets = sprite.Group()
boss = Boss(img_enemy, x=win_width//2, y=70, size_x=120, size_y=80, speed=12)
monsters = sprite.Group()
#создание группы спрайтов-астероидов ()
asteroids = sprite.Group()
booms = sprite.Group()

start_game()

last_time = time_t()
clock = time.Clock() 
#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна     
while run:
   #событие нажатия на кнопку “Закрыть”
   for e in event.get():
       if e.type == QUIT:
           run = False
       #событие нажатия на пробел - спрайт стреляет
       if e.type == KEYDOWN and e.key == K_SPACE and not finish:
            if limit_bull > 0 and time_t() - last_time > limit_time:
                fire_sound.play()
                ship.fire()
                limit_bull -= 1
                last_time = time_t()
              
   #сама игра: действия спрайтов, проверка правил игры, перерисовка
   if not finish:
        main_update()
    
        #проверка столкновения пули и монстров (и монстр, и пуля при касании исчезают)
        collides = sprite.groupcollide(monsters, ship.bullets, False, True)
        score = monsters_collide_actions(collides, score)
        collides = sprite.groupcollide(asteroids, ship.bullets, False, True)
        monsters_collide_actions(collides, 0)
        
        if final and boss.health > 0 and sprite.spritecollide(boss, ship.bullets, True):
            boss.health -= 1
            booms.add(Boom(x=boss.rect.centerx, y=boss.rect.bottom,  size_x=60, size_y=50))

        #если спрайт коснулся врага, уменьшает жизнь
        ship_collides_actions(monsters, True)
        ship_collides_actions(asteroids, True)
        ship_collides_actions(boss.bulletes, False)

        if score >= goal:
            final = True
        #проигрыш
        if life == 0 or lost >= max_lost:
            finish = True #проиграли, ставим фон и больше не управляем спрайтами.
            final_text = lose
        # Победа
        if boss.health <= 0:
            finish = True
            final_text = win
        
        display.update()
 
   #бонус: автоматический перезапуск игры
   else:
        while len(booms):
            main_update()
            window.blit(final_text, (win_width//2 - 200,  win_height//2 - 80))
            display.update()
            clock.tick(30)    
        for  _ in range(50):
            window.blit(final_text, (win_width//2 - 200,  win_height//2 - 80))
            display.update()
            clock.tick(30)  
        for b in ship.bullets:
            b.kill()
        for m in monsters:
            m.kill()
        for m in asteroids:
            m.kill()
        time.delay(3000)
        start_game()
 
   clock.tick(30)
