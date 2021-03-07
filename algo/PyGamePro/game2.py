from pygame import*
from pygame.sprite import Group
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, file_image, x, y, speed, size):
        # Вызываем конструктор класса (Sprite):
        super().__init__()

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(file_image), size)
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        #задаем его местонахождение
        self.rect.x = x
        self.rect.y = y

        self.speed = speed

    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    #метод, в котором реализовано управление спрайтом по кнопкам стрелочкам клавиатуры
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
        if sprite.spritecollide(self, walls, dokill=False):
            self.rect.x, self.rect.y = x, y
 
class Enemy(GameSprite):
    #класс спрайта-врага 
    def __init__(self, file_image, x, y, speed, size, left, right):
        super().__init__(file_image, x, y, speed, size)
        self.left = left
        self.right = right
        self.side = "left"
    
    def update(self):
        #движение врага
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

def main():
    def create_walls():
        #создаем стены
        global walls
        walls = sprite.Group()
        shema_walls = [
            {"x": 0,                'y': 0,                 'width': 5,         'height': win_height},
            {"x": 0,                'y': 0,                 'width': win_width, 'height': 5},
            {"x": (win_width - 5),  'y': 0,                 'width': 5,         'height': win_height},
            {"x": 0,                'y': (win_height - 5),  'width': win_width, 'height': 5},
            {"x": 300,              'y': 50,                'width': 10,        'height': win_height},
            {"x": 450,              'y': 250,                'width': 10,        'height': 300},
            {"x": 350,              'y': 250,               'width': 150,       'height': 10},
            {"x": 550,              'y': 250,               'width': 150,       'height': 10},
            {"x": 300,              'y': 50,                'width': 350,       'height': 10},
            {"x": 300,              'y': 50,                'width': 10,        'height': 350}
        ]
        # добавляем в группу стен
        for shema_wall in shema_walls:
            walls.add(Wall(color=(0, 0, 250), **shema_wall))

    def create_sprites():
        #создаем спрайты
        global packman, monster, final_sprite
        packman = Player(file_image='Герои/pacman/pac-1.png',
                        x=5, y=(win_height - 80), speed=3, size=hero_size)
        monster = Enemy(file_image='Герои/pacman/cyborg.png',
                        x=win_width - 80, y=200, speed=3, size=hero_size,
                        left=480, right=(win_width - 85))
        final_sprite = GameSprite(file_image='Герои/pacman/pac-10.png',
                            x=win_width - 85, y=win_height - 100,
                            speed=0, size=hero_size)

    def game_loop():
        #игровой цикл
        finish = False  #переменная, отвечающая за то, как кончилась игра
        clock = time.Clock()
        run = True
        while run:
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

                #Проверка столкновения героя с врагом
                if sprite.collide_rect(packman, monster):
                    finish = True
                    window.blit(game_over, (0, 0))
                    kick.play()
                    mixer.music.stop()
                #Проверка столкновения героя с финальным спрайтом
                if sprite.collide_rect(packman, final_sprite):
                    finish = True
                    window.blit(final_img, (0, 0))
                    money.play()
                    mixer.music.stop()
            else:
                time.delay(4000)
                run = False
            
            clock.tick(fps)
            display.update()
 
    # Изображение для победы
    final_img = transform.scale(image.load('Фоны/winner_1.jpg'), (win_width, win_height))
    # Изображение для поражения
    game_over = transform.scale(image.load('gameover.jpeg'), (win_width, win_height))

    #музыка
    mixer.music.load('fon.ogg')
    mixer.music.set_volume(0.3)
    mixer.music.play()

    money = mixer.Sound('money.ogg')
    kick = mixer.Sound('kick.ogg')

    create_walls()
    create_sprites()
    fps = 60  # частота кадро 60 в секунду
    game_loop()


init()
#Создаем окошко
win_width = 700
win_height = 500
hero_size = 40, 40
display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
main()