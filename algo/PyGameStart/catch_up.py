from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, hero_size):
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), hero_size)
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Догонялки")

#задай фон сцены
background = transform.scale(image.load("/home/whector/Documents/GitHub/lessons/algo/PyGameStart/background.png"), (700, 500))
winner = transform.scale(image.load("/home/whector/Documents/GitHub/lessons/algo/PyGameStart/background.png"), (700, 500))

#создай 2 спрайта и размести их на сцене
hero_size = 50, 50
start_x, start_y = 40, 400
speed = 10
sp1 = GameSprite('sprite1.png', start_x, start_y, speed, hero_size)
x2, y2 = 150, 400
speed2 = 5
sp2 = GameSprite('sprite2.png', x2, y2, speed2, hero_size)
new_x2, new_y2 = x2, y2

clock = time.Clock()
FPS = 60

def enemy_move():
    global new_x2, new_y2
    if new_x2 == sp2.rect.x and new_y2 == sp2.rect.y:
       new_x2, new_y2 = randint(1, 65) * 10, randint(1, 45) * 10
    if sp2.rect.x > new_x2:
       sp2.rect.x -= speed2
    elif sp2.rect.x < new_x2:
       sp2.rect.x += speed2
    if sp2.rect.y > new_y2:
       sp2.rect.y -= speed2
    elif sp2.rect.y < new_y2:
       sp2.rect.y += speed2


def controller():
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and sp1.rect.x > 5:
       sp1.rect.x -= speed
    if keys_pressed[K_RIGHT] and sp1.rect.x < 650:
       sp1.rect.x += speed
    if keys_pressed[K_UP] and sp1.rect.y > 5:
       sp1.rect.y -= speed
    if keys_pressed[K_DOWN] and sp1.rect.y < 450:
       sp1.rect.y += speed

run = True
while run:
    for e in event.get():
       if e.type == QUIT:  #обработай событие «клик по кнопке "Закрыть окно"»
          run = False
    if sprite.collide_rect(sp1, sp2):
        window.blit(winner,(0, 0))
    else:
        controller()
        enemy_move()
        window.blit(background,(0, 0))
        sp1.reset()
        sp2.reset() 
    display.update()
    clock.tick(FPS)