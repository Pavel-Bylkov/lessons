from pygame import *
from random import randint
from time import time as time_t
 
# нам нужны такие картинки:
img_win = "thumb.jpg" # фон победы
img_los = "game-over.png" # фон проигрыша
img_back = "galaxy.jpg" # фон игры
 
img_bullet = "bullet.png" # пуля
img_hero = "rocket.png" # герой
img_enemy = "ufo.png" # враг

win_width = 900
win_height = 600 
score = 0 # сбито кораблей
goal = 15 # столько кораблей нужно сбить для победы
lost = 0 # пропущено кораблей
max_lost = 5 # проиграли, если пропустили столько
last_time = time_t()
pause_fire = 0.2  # Пауза между выстрелами
 
# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
  def __init__(self, player_image, x, y, size_x, size_y, speed, direction):
      # Вызываем конструктор класса (Sprite):
      #sprite.Sprite.__init__(self)
      super().__init__()
      self.direction = direction
 
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
  # метод для управления спрайтом стрелками клавиатуры
  def update(self):
      global last_time
      keys = key.get_pressed()
      if keys[K_LEFT] and self.rect.x > 5:
          self.rect.x -= self.speed
      if keys[K_RIGHT] and self.rect.x < win_width - 80:
          self.rect.x += self.speed
      # событие нажатия на пробел - спрайт стреляет
      if keys[K_SPACE] and time_t() - last_time > pause_fire:
          self.fire()
          last_time = time_t()
      self.bullets.update()
  # метод "выстрел" (используем место игрока, чтобы создать там пулю)
  def fire(self):
      bullet = Bullet(img_bullet, x=self.rect.centerx, y=self.rect.top, size_x=15, size_y=20, speed=15, direction=self.direction)
      self.bullets.add(bullet)
  def reset(self):
      super().reset()
      self.bullets.draw(window)
# класс спрайта-врага   
class Enemy(GameSprite):
    def __init__(self, player_image, x, y, size_x, size_y, speed, direction):
      super().__init__(player_image, x, y, size_x, size_y, speed, direction)
      self.bullets = sprite.Group()
    # движение врага
    def update(self):
        keys = key.get_pressed()
        if keys[K_5]:
            self.fire()
        self.rect.y += self.speed
        global lost
        # исчезает, если дойдет до края экрана
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

    def fire(self):
      bullet = Bullet(img_bullet, x=self.rect.centerx, y=self.rect.bottom, size_x=15, size_y=20, speed=15, direction=self.direction)
      self.bullets.add(bullet)
    def reset(self):
      super().reset()
      self.bullets.draw(window)
 
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

# подгружаем отдельно функции для работы со шрифтом
init()
font.init()
# во время игры пишем надписи размера 36
font = font.Font(None, 36) 
# Создаем окошко
display.set_caption("Шутер")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
 
# создаем спрайты
ship = Player(img_hero, x=5, y=win_height - 100, size_x=80, size_y=100, speed=10, direction=-1)
 
# создание группы спрайтов-врагов
monsters = sprite.Group()
for i in range(1, 6):
  monster = Enemy(img_enemy, x=randint(80, win_width - 80), y=-40, size_x=80, size_y=50, speed=randint(1, 5), direction=1)
  monsters.add(monster)
 
# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
clock = time.Clock()
FPS = 20
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
  
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
        #elif e.type == KEYDOWN:
          #if e.key == K_SPACE:
              #ship.fire()

    # сама игра: действия спрайтов, проверка правил игры, перерисовка
    if not finish:
        # обновляем фон
        window.blit(background,(0,0))
    
        # пишем текст на экране
        text = font.render("Счет: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
    
        text_lose = font.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
    
        # производим движения спрайтов
        ship.update()
        monsters.update()
        
        # обновляем их в новом местоположении при каждой итерации цикла
        ship.reset()
        monsters.draw(window)
        
        # проверка столкновения пули и монстров (и монстр, и пуля при касании исчезают)
        collides = sprite.groupcollide(monsters, ship.bullets, True, True)
        for c in collides:
            # этот цикл повторится столько раз, сколько монстров подбито
            score = score + 1
            monster = Enemy(img_enemy, x=randint(80, win_width - 80), y=-40, size_x=80, size_y=50, speed=randint(1, 5), direction=1)
            monsters.add(monster)
    
        # возможный проигрыш: пропустили слишком много или герой столкнулся с врагом
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True # проиграли, ставим фон и больше не управляем спрайтами.
            # вычисляем отношение
            img = image.load(img_los)
            window.fill((0,0,0))
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
    
        # проверка выигрыша: сколько очков набрали?
        if score >= goal:
            finish = True
            img = image.load(img_win)
            window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
    
        display.update()
    # цикл срабатывает каждую 0.05 секунд
    clock.tick(FPS)