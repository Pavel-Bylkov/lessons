from pygame import *

#класс-родитель для спрайтов 
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, sprite_image, x, y, speed, hero_size):
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(sprite_image), hero_size)
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed  # с каким шагом будут меняться координаты спрайтов

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

init()
GREEN = (0, 255, 0)  # цвет для стен
#Игровая сцена:
win_width, win_height = 1600, 900
hero_size = 60, 60
window = display.set_mode((win_width, win_height))
display.set_caption("Лабиринт")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

#Персонажи игры:
player = GameSprite('kolobok.png', x=5, y=win_height - 80, speed=4, hero_size=hero_size)
monster = GameSprite('cyborg.png', x=win_width - 80, y=280, speed=2, hero_size=hero_size)
final = GameSprite('treasure.png', x=win_width - 120, y=win_height - 80, speed=0, hero_size=hero_size)

def change_image(sprite, new_image, new_size):
    center = sprite.rect.center
    sprite.image = transform.scale(image.load(new_image), new_size)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.center = center

# Стены
walls = sprite.Group()
walls.add(Wall(x=30, y=50, width=600, height=10))
walls.add(Wall(x=330, y=50, width=10, height=400))

clock = time.Clock()
FPS = 60

#музыка "mp3", "ogg", "mid", "mod", "it", "xm", "wav"
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.25)  # Задаем громкость от 0 до 1
mixer.music.play()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and e.key == K_c:
             change_image(sprite=player, new_image="kolobok2.png", new_size=hero_size)
    
    window.blit(background,(0, 0))
    walls.draw(window)
    player.reset()
    monster.reset()
    final.reset()
    
    display.update()
    clock.tick(FPS)