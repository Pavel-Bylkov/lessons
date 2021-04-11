from pygame import *
img_back = "galaxy.jpg" # фон игры
img_hero = "rocket.png" # герой

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

# Создаем окошко
win_width, win_height = 800, 500
display.set_caption("Shuter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# создаем спрайты
ship = Player(img_hero, x=win_width//2, y=win_height - 100,
                            size_x=60, size_y=80, speed=10)

finish = False
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # перебираем полученные события
    for e in event.get():
        # событие нажатия на крестик окошка
        if e.type == QUIT:
            run = False
    if not finish:
        # обновляем фон
        window.blit(background,(0,0))
        # производим движения спрайтов
        ship.update()
        # обновляем их в новом местоположении при каждой итерации цикла
        ship.reset()

        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)