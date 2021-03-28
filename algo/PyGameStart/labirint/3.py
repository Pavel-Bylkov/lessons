from pygame import *
from time import sleep
'''Необходимые классы'''

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
            print("x = ", self.rect.x + 30, 'y = ', self.rect.y + 30)

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
#класс для спрайтов-препятствий
class Wall(sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
init()
GREEN = (0, 255, 0)
#Игровая сцена:
win_width, win_height = 1600, 880
hero_size = 60, 60
window = display.set_mode((win_width, win_height)) #FULLSCREEN
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

#Персонажи игры:
start_x, start_y = 5, win_height - 80
player = Player('hero.png', x=start_x, y=start_y, speed=5, hero_size=hero_size)
monster = Enemy('cyborg.png', x=1400, y=280, speed=4 , hero_size=hero_size,
                    left_up=460, right_down=1400, direction='left')
monster2 = Enemy('cyborg.png', x=win_width//2, y=280, speed=4 , hero_size=hero_size,
                    left_up=5, right_down=win_height - 460, direction='up')
final = GameSprite('treasure.png', x=win_width - 120, y=win_height - 80,
                            speed=0 , hero_size=hero_size)

# Стены
walls = sprite.Group()
walls.add(Wall(x=80, y=100, width=520, height=10))
walls.add(Wall(x=460, y=100, width=10, height=400))
walls.add(Wall(x=1080, y=100, width=520, height=10))
walls.add(Wall(x=1460, y=100, width=10, height=400))
walls.add(Wall(x=win_width//2+100, y=win_height-400, width=10, height=400))

# Картинки Победы и Поражения (получаем из текста)
font.init()
font2 = font.Font(None, 170)
#font2 = font.SysFont('arial', 170)
win = font2.render('YOU WIN!', True, (255, 215, 0))
lose = font2.render('YOU LOSE!', True, (180, 0, 0))

#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.3)
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_q):
            game = False
    
    if finish != True:
        window.blit(background,(0, 0))
        walls.draw(window)
        player.update()
        monster.update()
        monster2.update()
        
        player.reset()
        monster.reset()
        monster2.reset()
        final.reset() 

        #Ситуация "Проигрыш"
        #if sprite.spritecollide(player, monsters, dokill=False): для грцппы
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, monster2):
            window.blit(lose, (win_width // 2 - 350, win_height // 2 - 100))
            kick.play()
            display.update()
            sleep(1) 
            player.rect.x, player.rect.y = start_x, start_y

        #Ситуация "Выигрыш"
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (win_width // 2 - 350, win_height // 2 - 100))
            money.play()
    else:
        sleep(5)
        game = False
    display.update()
    clock.tick(FPS)