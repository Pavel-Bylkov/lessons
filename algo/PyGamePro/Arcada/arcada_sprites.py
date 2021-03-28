from constants_globalvars import *
from arcada_classes import FinalSprite, Hero, Wall, Enemy
# список всех персонажей игры:
all_sprites = pygame.sprite.Group()
# список препятствий:
barriers = pygame.sprite.Group()
# список врагов:
enemies = pygame.sprite.Group()
# список мин:
bombs = pygame.sprite.Group()

# создаем персонажа, добавляем его в список всех спрайтов:
robin = Hero(img_file_hero) 
all_sprites.add(robin)
# создаем стены, добавляем их:
w = Wall(50, 150, 480, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(700, 50, 50, 360) 
barriers.add(w)
all_sprites.add(w)
w = Wall(350, 380, 640, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(-200, 590, 1600, 20)
barriers.add(w)
all_sprites.add(w)

# создаем врагов, добавляем их:
en = Enemy(50, 480)
all_sprites.add(en)
enemies.add(en)

en = Enemy(400, 480)
all_sprites.add(en)
enemies.add(en)

# создаем мины, добавляем их:
bomb = Enemy(550, 520, img_file_bomb, 60, 60)
bombs.add(bomb) # в список всех спрайтов бомбы не добавляем, будем рисовать их отдельной командой
                # так легко сможем подрывать бомбы, а также делаем их неподвижными, update() не вызывается

# создаем финальный спрайт, добавляем его:
pr = FinalSprite(img_file_princess, win_width + 500, win_height - 150, 0)
all_sprites.add(pr)