from pygame import *
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
            print("x = ", self.rect.x + 30, 'y = ', self.rect.y + 30)
            time.delay(500)

#класс-наследник для спрайта-врага (перемещается сам)
class Enemy(GameSprite):
    def __init__(self, player_image, x, y, speed, hero_size, direction, left, right):
        super().__init__(player_image, x, y, speed, hero_size)
        self.direction = direction
        self.left = left
        self.right = right
    def update(self):
        if self.rect.x <= self.left:
            self.direction = "right"
        elif self.rect.x >= self.right:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

init()
GREEN = (20, 230, 20)
#Игровая сцена:
win_width, win_height = 1600, 800
hero_size = 60, 60
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

#Персонажи игры:
player = Player('hero.png', x=5, y=win_height - 80, speed=4, hero_size=hero_size)
monsters = sprite.Group()
monsters.add(Enemy('cyborg.png', x=1460 - 80, y=280, speed=2 , hero_size=hero_size,
                    direction='left', left=470, right=1460 - 80))
monsters.add(Enemy('cyborg.png', x=900, y=450, speed=2 , hero_size=hero_size,
                    direction='left', left=470, right=900))
final = GameSprite('treasure.png', x=win_width - 120, y=win_height - 80,
                            speed=0 , hero_size=hero_size)

# Стены
walls = sprite.Group()
walls.add(Wall(x=80, y=100, width=520, height=10))
walls.add(Wall(x=460, y=100, width=10, height=400))
walls.add(Wall(x=1080, y=100, width=520, height=10))
walls.add(Wall(x=1460, y=100, width=10, height=400))
walls.add(Wall(x=580, y=400, width=520, height=10))
walls.add(Wall(x=960, y=400, width=10, height=400))

game = True
finish = False
clock = time.Clock()
FPS = 60

#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.3)
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0, 0))
        walls.draw(window)
        player.update()
        monsters.update()
        player.reset()
        monsters.draw(window)
        final.reset() 

    display.update()
    clock.tick(FPS)