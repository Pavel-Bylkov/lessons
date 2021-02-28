from pygame import*
from pygame.sprite import Group
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, hero_size):
        # Вызываем конструктор класса (Sprite):
        super().__init__()

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), hero_size)
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        #задаем его местонахождение
        self.rect.x = player_x
        self.rect.y = player_y

        self.speed = player_speed

    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    #метод, в котором реализовано управление спрайтом по кнопкам стрелочкам клавиатуры
    def step_back(self, x, y):
        if sprite.spritecollide(self, walls, dokill=False):
            self.rect.x, self.rect.y = x, y

    def update(self):
        keys = key.get_pressed()
        x, y = self.rect.x, self.rect.y
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
        self.step_back(x, y)

#класс спрайта-врага    
class Enemy(GameSprite):
    side = "left"
    #движение врага
    def update(self):
        if self.rect.x <= 410:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

#класс элемента стены
class Wall(sprite.Sprite):
    def __init__(self, color,  x, y, width, height):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height

        # картинка стены - прямоугольник нужных размеров и цвета
        self.image = Surface([self.width, self.height]) #создаем поверхность нужной ширины и длины
        self.image.fill(self.color) #заполняем ее цветом
 
       # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        draw.rect(window, self.color, (self.rect.x, self.rect.y, self.width, self.height))

init()
#Создаем окошко
win_width = 700
win_height = 500
hero_size = 40, 40
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))

#создаем стены
walls = sprite.Group()
shema_walls = [
    {"x": 0,                'y': 0,                 'width': 5,         'height': win_height},
    {"x": 0,                'y': 0,                 'width': win_width, 'height': 5},
    {"x": (win_width - 5),  'y': 0,                 'width': 5,         'height': win_height},
    {"x": 0,                'y': (win_height - 5),  'width': win_width, 'height': 5},
    {"x": 300,              'y': 50,                'width': 10,        'height': 350},
    {"x": 350,              'y': 250,               'width': 150,       'height': 10},
    {"x": 550,              'y': 250,               'width': 150,       'height': 10},
    {"x": 300,              'y': 50,                'width': 350,       'height': 10},
    {"x": 300,              'y': 50,                'width': 10,        'height': 350}
]
# добавляем в группу стен
for shema_wall in shema_walls:
    walls.add(Wall(color=(0, 0, 250), **shema_wall))

#создаем спрайты
packman = Player(player_image='Герои/pacman/pac-1.png', 
                    player_x=5, player_y=(win_height - 80), player_speed=5, hero_size=hero_size)
monster = Enemy(player_image='Герои/pacman/cyborg.png',
                    player_x=win_width - 80, player_y=200, player_speed=5, hero_size=hero_size)
final_sprite = GameSprite(player_image='Герои/pacman/pac-10.png',
                    player_x=win_width - 85, player_y=win_height - 100, player_speed=0, hero_size=hero_size)

#переменная, отвечающая за то, как кончилась игра
finish = False

fps = 60
clock = time.Clock()

#игровой цикл
run = True
while run:
    #цикл срабатывает каждую 0.05 секунд
    clock.tick(fps)
    #перебираем все события, которые могли произойти
    for e in event.get():
        #событие нажатия на кнопку “закрыть”
        if e.type == QUIT:
            run = False
    if not finish:
        #обновляем фон каждую итерацию
        window.fill((0, 0, 0))
        #рисуем стены
        for wall in walls.sprites():
            wall.draw_wall()
         #запускаем движения спрайтов
        packman.update()
        monster.update()
        #обновляем их в новом местоположении при каждой итерации цикла
        packman.reset()
        monster.reset()
        final_sprite.reset()
    else:
        time.delay(4000)
        run = False
    #Проверка столкновения героя с врагом
    if sprite.collide_rect(packman, monster):
        finish = True
        #вычисляем отношение
        img = image.load('gameover.jpeg')
        d = img.get_width() // img.get_height()
        window.fill((0, 0, 0))
        window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))

    if sprite.collide_rect(packman, final_sprite):
        finish = True
        img = image.load('Фоны/winner_1.jpg')
        window.fill((0, 0, 0))
        window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
    
    display.update()

