from pygame import *
from time import sleep, time as time_t
from map import maps
'''Необходимые классы'''
#класс-родитель для спрайтов 
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, x, y, speed, hero_size):
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), hero_size)
        self.speed = speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_image(self, new_image, new_size):
        center = self.rect.center
        self.image = transform.scale(image.load(new_image), new_size)
        self.rect = self.image.get_rect()
        self.rect.center = center

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
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
        if keys[K_p]:
            print("x = ", self.rect.centerx, 'y = ', self.rect.centery)
            time.delay(500)

#класс-наследник для спрайта-врага (перемещается сам)
class Enemy(GameSprite):
    def __init__(self, player_image, x, y, speed, hero_size, 
                                    left_up, right_down, direction):
        super().__init__(player_image, x, y, speed, hero_size)
        self.right_down = right_down
        self.left_up = left_up
        self.direction = direction
    def update(self):
        if self.direction == 'left' and self.rect.x <= self.left_up:
            self.direction = "right"
        elif self.direction == 'right' and self.rect.x >= self.right_down:
            self.direction = "left"
        elif self.direction == 'up' and self.rect.y <= self.left_up:
            self.direction = "down"
        elif self.direction == 'down' and self.rect.y >= self.right_down:
            self.direction = "up"

        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
# класс для стен, особенность - изображение прямоугольник
class Wall(sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

init()

#Игровая сцена:
win_width, win_height = 1465, 885
window = display.set_mode((win_width, win_height)) #FULLSCREEN
display.set_caption("Maze")
# Создаем фоновое изображение по размеру окна
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

#Персонажи игры:
hero_size = 60, 60
start_x, start_y = 5, win_height - 80
player = Player('hero.png', x=start_x, y=start_y, speed=5, hero_size=hero_size)
monsters = sprite.Group()
monsters.add(
        Enemy('cyborg.png', x=1400, y=280, speed=4 , hero_size=hero_size,
                    left_up=460, right_down=1400, direction='left'),
        Enemy('cyborg.png', x=win_width//2, y=280, speed=4 , hero_size=hero_size,
                    left_up=5, right_down=win_height - 460, direction='up')
            )
final = GameSprite('treasure.png', x=(win_width - 120), y=(win_height - 80),
                            speed=0 , hero_size=hero_size)

traps = sprite.Group()
traps.add(GameSprite("trap.png", x=220, y=(win_height - 280), speed=0 , hero_size=hero_size),
    GameSprite("trap.png", x=820, y=580, speed=0 , hero_size=hero_size))

# Стены
GREEN = (0, 255, 0)
walls = sprite.Group()
for i in range(len(maps)):
    for j in range(len(maps[i])):
        if maps[i][j] == 1:
            walls.add(Wall(x=j * 25, y=i * 25, width=10, height=10))

walls.add(Wall(x=80, y=100, width=520, height=10))
walls.add(Wall(x=460, y=100, width=10, height=400))
walls.add(Wall(x=1080, y=100, width=520, height=10))
walls.add(Wall(x=1260, y=100, width=10, height=200))
walls.add(Wall(x=580, y=400, width=520, height=10))
walls.add(Wall(x=960, y=400, width=10, height=400))
walls.add(Wall(x=250, y=300, width=200, height=10))

# Картинки Победы и Поражения (получаем из текста)
font.init()
font2 = font.Font(None, 170)
#font2 = font.SysFont('arial', 170)
win = font2.render('YOU WIN!', True, (255, 215, 0))
lose = font2.render('YOU LOSE!', True, (180, 0, 0))

#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.2)
mixer.music.play()

money = mixer.Sound('money.ogg')
money.set_volume(0.5)
kick = mixer.Sound('kick.ogg')
kick.set_volume(0.5)

game = True
finish = False
clock = time.Clock()
FPS = 50

def draw_all():
    window.blit(background,(0, 0))
    walls.draw(window)          
    monsters.draw(window)
    traps.draw(window)
    final.reset() 
    player.reset()

def draw_final(final_img):
    window.blit(final_img, (win_width // 2 - 350, win_height // 2 - 100))
    display.update()

while game:
    for e in event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_q):
            game = False
    
    if finish != True:
        player.update()
        monsters.update()
        draw_all()     

        #Ситуация "Проигрыш"
        if (sprite.spritecollide(player, monsters, dokill=False)):  # для грцппы
            kick.play()
            player.change_image(new_image="sprite2.png", new_size=hero_size)
            draw_all()
            draw_final(lose)
            sleep(1) 
            player.change_image(new_image="hero.png", new_size=hero_size)
            player.rect.x, player.rect.y = start_x, start_y

        if (sprite.spritecollide(player, traps, dokill=False)):  # для грцппы
            player.speed = 1
        else:
            player.speed = 5

        #Ситуация "Выигрыш"
        if sprite.collide_rect(player, final):
            finish = True
            draw_final(win)
            money.play()
            last_time = time_t()
    elif time_t() - last_time > 5:
        game = False
    display.update()
    clock.tick(FPS)