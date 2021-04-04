from pygame import *
from random import randint
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, x, y, speed):
        # Вызываем конструктор класса (Sprite):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), hero_size)
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
    #метод, в котором реализовано управление спрайтом по кнопкам стрелочкам клавиатуры
    def update(self):
        keys = key.get_pressed()
        x, y = self.rect.x, self.rect.y
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if sprite.spritecollide(self, walls, dokill=False):
            self.rect.x, self.rect.y = x, y
#класс спрайта-врага    
class Enemy(GameSprite):
    def __init__(self, player_image, x, y, speed, side, left, right):
        super().__init__(player_image, x, y, speed)
        self.side = side
        self.left = left
        self.right = right
    #движение врага
    def update(self):
        if self.rect.x <= self.left:
            self.side = "right"
        if self.rect.x >= self.right:
            self.side = "left"
        x, y = self.rect.x, self.rect.y
        if self.side == "left":
            self.rect.x -= self.speed
            if sprite.spritecollide(self, walls, dokill=False):
                self.rect.x, self.rect.y = x, y
                self.side = "right"
        else:
            self.rect.x += self.speed
            if sprite.spritecollide(self, walls, dokill=False):
                self.rect.x, self.rect.y = x, y
                self.side = "left"
        
#класс элемента стены
class Wall(sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        # картинка стены - прямоугольник нужных размеров и цвета
        self.image = Surface([width, height])
        self.image.fill(COLOR_WALL)
        # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#Создаем окошко
map = []
with open("map1.labirint", "r", encoding="utf-8") as file:
    for line in file:
        map.append(list(line)[:-1])
win_width = 1650
win_height = 860
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
#создаем стены
COLOR_WALL = (0, 0, 255)
walls = sprite.Group()
monsters = sprite.Group()
packman = final_sprite = None
hero_size = 60, 60
kx = (win_width - 15) // (len(map[0]) - 1)
ky = (win_height - 15) // (len(map) - 1)
for y in range(len(map)):
    for x in range(len(map[y])):
        # создаем основу лабиринта
        if map[y][x] == '1':
            walls.add(Wall(x=x*kx, y=y*ky, width=15, height=15))
        if map[y][x] == '3':
            monsters.add(Enemy('cyborg.png', x=x*kx, y=y*ky - 20, speed=5,
                            side="left"*randint(0,1), left=x*kx - 300, right=x*kx + 300))
        if map[y][x] == '2':
            packman = Player('hero.png', x=x*kx, y=y*ky - 20, speed=7)
        if map[y][x] == '4':
            final_sprite = GameSprite('treasure.png', x=x*kx, y=y*ky - 20, speed=0)
    # делаем дополнительные линии если рядом продолжается стена
    for x in range(len(map[y])):
        if y > 0 and y != len(map) -1 and map[y-1][x] == '1' and map[y][x] == '1':
            walls.add(Wall(x=x*kx, y=y*ky - 60, width=15, height=60))
    for x in range(len(map[y])):
        if y > 0 and y != len(map) -1 and map[y+1][x] == '1' and map[y][x] == '1':
            walls.add(Wall(x=x*kx, y=y*ky + 15, width=15, height=60))
    for x in range(1, len(map[y]) - 1):
        if map[y][x-1] == '1' and map[y][x] == '1':
            walls.add(Wall(x=x*kx - 30, y=y*ky, width=30, height=15))
    for x in range(1, len(map[y]) - 1):
        if map[y][x+1] == '1' and map[y][x] == '1':
            walls.add(Wall(x=x*kx + 15, y=y*ky, width=30, height=15))
# проверяем наличие на карте спрайтов, если нет добавляем по умолчанию 
if packman is None:
    packman = Player('hero.png', x=5, y=win_height - 80, speed=5)
if len(monsters) == 0:
    monsters.add(Enemy('cyborg.png', x=win_width - 80, y=200, speed=5,
                            side="left", left=win_width//2, right=win_width - 85))
if final_sprite is None:
    final_sprite = GameSprite('treasure.png', x=win_width - 85, y=win_height - 100, speed=0)
#переменная, отвечающая за то, как кончилась игра
finish = False
#игровой цикл
run = True
while run:
    #цикл срабатывает каждую 0.05 секунд (20 кадров в секунду)
    time.delay(50)
    #перебираем все события, которые могли произойти
    for e in event.get():
        #событие нажатия на кнопку “закрыть”
        if e.type == QUIT:
            run = False
    #проверка, что игра еще не завершена
    if not finish:
        #обновляем фон каждую итерацию
        window.fill((255, 255, 255))
        #рисуем стены
        walls.draw(window)
        #запускаем движения спрайтов
        packman.update()
        monsters.update()
        #обновляем их в новом местоположении при каждой итерации цикла
        packman.reset()
        monsters.draw(window)
        final_sprite.reset()
        #Проверка столкновения героя с врагом и стенами
        if sprite.spritecollide(packman, monsters, False):
            finish = True
            img = transform.scale(image.load('gameover.jpeg'), (win_width, win_height))
            window.blit(img, (0, 0))
        if sprite.collide_rect(packman, final_sprite):
            finish = True
            img = transform.scale(image.load('winner_1.jpg'), (win_width, win_height))
            window.blit(img, (0, 0))
    display.update()
