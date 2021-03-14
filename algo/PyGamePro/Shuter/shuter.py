from pygame import *
from random import randint
# подгружаем отдельно функции для работы со шрифтом
font.init()
# во время игры пишем надписи размера 36
font = font.Font(None, 36)

# нам нужны такие картинки:
img_win = "thumb.jpg" # фон победы
img_los = "game-over.png" # фон проигрыша
img_back = "galaxy.jpg" # фон игры

img_bullet = "bullet.png" # пуля
img_hero = "rocket.png" # герой
img_enemy = "ufo.png" # враг

score = 0 # сбито кораблей
goal = 10 # столько кораблей нужно сбить для победы
lost = 0 # пропущено кораблей
max_lost = 3 # проиграли, если пропустили столько

# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
   # конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       # Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)

       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed

       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

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
       bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
       bullets.add(bullet)
# класс спрайта-врага    
class Enemy(GameSprite):
   # движение врага
   def update(self):
       self.rect.y += self.speed
       
       # исчезает, если дойдет до края экрана
       if self.rect.y > win_height:
           self.rect.x = randint(80, win_width - 80)
           self.rect.y = 0
           global lost
           lost = lost + 1

# класс спрайта-пули    
class Bullet(GameSprite):
   # движение врага
   def update(self):
       self.rect.y += self.speed
       # исчезает, если дойдет до края экрана
       if self.rect.y < 0:
           self.kill()

# Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Лабиринт")
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

# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты 
finish = False
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
   # перебираем полученные события
   for e in event.get():
       # событие нажатия на крестик окошка
       if e.type == QUIT:
           run = False
       # событие нажатия на пробел - спрайт стреляет
       elif e.type == KEYDOWN:
           if e.key == K_SPACE:
               ship.fire()

   # сама игра: действия спрайтов, проверка правил игры, перерисовка
   if not finish:
       # обновляем фон
       window.blit(background,(0,0))

       # пишем текст на экране
       text = font.render("Счет: " + str(score), 1, (255, 255, 255))
       place = text.get_rect(center = (50, 20))
       window.blit(text, place)

       text_lose = font.render("Пропущено: " + str(lost), 1, (255, 255, 255))
       place = text_lose.get_rect(center = (95, 50))
       window.blit(text_lose, place)

       # производим движения спрайтов
       ship.update()
       monsters.update()
       bullets.update()

       # обновляем их в новом местоположении при каждой итерации цикла
       ship.reset()
       monsters.draw(window)
       bullets.draw(window)

       # проверка столкновения пули и монстров (и монстр, и пуля при касании исчезают)
       collides = sprite.groupcollide(monsters, bullets, True, True)
       for c in collides:
           # этот цикл повторится столько раз, сколько монстров подбито
           score = score + 1
           monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
           monsters.add(monster)

       # возможный проигрыш: пропустили слишком много или герой столкнулся с врагом
       if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
           finish = True # проиграли, ставим фон и больше не управляем спрайтами.
           # вычисляем отношение
           img = image.load(img_los)
           d = img.get_width() // img.get_height()
           window.fill((255, 255, 255))
           window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))
    
       # проверка выигрыша: сколько очков набрали?
       if score >= goal:
           finish = True
           img = image.load(img_win)
           window.fill((255, 255, 255))
           window.blit(transform.scale(img, (win_width, win_height)), (0, 0))

       display.update()
   # цикл срабатывает каждую 0.05 секунд
   time.delay(50)

