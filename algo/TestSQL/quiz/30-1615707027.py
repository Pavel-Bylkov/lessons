from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, hero_size):
        super().__init__()

        self.image = transform.scale(image.load(player_image), hero_size)
        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

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
GREEN = (0, 255, 0)
win_width, win_height = 700, 500
hero_size = 60, 60
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

player = GameSprite('hero.png', x=5, y=win_height - 80, speed=4, hero_size=hero_size)
monster = GameSprite('cyborg.png', x=win_width - 80, y=280, speed=2, hero_size=hero_size)
final = GameSprite('treasure.png', x=win_width - 120, y=win_height- 80, speed=0, hero_size=hero_size)

walls = sprite.Group()
walls.add(Wall(x=30, y=50, width=600, height=10))
walls.add(Wall(x=330, y=50, width=10, height=4000))


clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.6)
mixer.music.play()
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0, 0))
    walls.draw(window)
    player.reset()
    monster.reset()
    final.reset()

    display.update()
    clock.tick(FPS)