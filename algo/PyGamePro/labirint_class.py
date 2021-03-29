from pygame import *
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, x, y, speed):
        # Вызываем конструктор класса (Sprite):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (80, 80))
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
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
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
win_width = 1600
win_height = 900
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
#создаем стены
COLOR_WALL = (0, 0, 255)
walls = sprite.Group()
walls.add(
    Wall(x=100, y=win_height / 2, width=320, height=10),
    Wall(x=100, y=2 * win_height / 4, width=620, height=10),
    Wall(x=410, y=win_height / 4, width=10, height=350)
    )

#создаем спрайты
packman = Player('hero.png', x=5, y=win_height - 80, speed=5)
monster = Enemy('cyborg.png', x=win_width - 80, y=200, speed=5,
                            side="left", left=450, right=win_width - 85)
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
        monster.update()
        #обновляем их в новом местоположении при каждой итерации цикла
        packman.reset()
        monster.reset()
        final_sprite.reset()
        #Проверка столкновения героя с врагом и стенами
        if sprite.collide_rect(packman, monster):
            finish = True
            img = transform.scale(image.load('gameover.jpeg'), (win_width, win_height))
            window.blit(img, (0, 0))
        if sprite.collide_rect(packman, final_sprite):
            finish = True
            img = transform.scale(image.load('winner_1.jpg'), (win_width, win_height))
            window.blit(img, (0, 0))
    display.update()
