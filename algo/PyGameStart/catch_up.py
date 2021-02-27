from pygame import *
from random import randint

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Догонялки")

#задай фон сцены
background = transform.scale(image.load("background.png"), (700, 500))
winner = transform.scale(image.load("gameover.jpg"), (700, 500))

#создай 2 спрайта и размести их на сцене
sp1 = transform.scale(image.load("sprite1.png"), (50, 50))
sp2 = transform.scale(image.load("sprite2.png"), (50, 50))
x1, y1 = 40, 400
x2, y2 = 150, 400
new_x2, new_y2 = x2, y2
speed = 10
speed2 = 5

clock = time.Clock()
FPS = 60

def enemy_move():
    global x2, y2 , new_x2, new_y2
    if new_x2 == x2 and new_y2 == y2:
        new_x2, new_y2 = randint(1, 65) * 10, randint(1, 45) * 10
    if x2 > new_x2:
       x2 -= speed2
    elif x2 < new_x2:
       x2 += speed2
    if y2 > new_y2:
       y2 -= speed2
    elif y2 < new_y2:
        y2 += speed2

def is_catch_up():
    """if x1 > x2 and x2 + 50 >= x1 and (y1 > y2"""
    return False

def controller():
    global x1, y1
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 5:
       x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 650:
       x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
       y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 450:
       y1 += speed

run = True
while run:
    for e in event.get():
       if e.type == QUIT:  #обработай событие «клик по кнопке "Закрыть окно"»
          run = False
    if is_catch_up():
        window.blit(winner,(0, 0))
    else:
        controller()
        enemy_move()
        window.blit(background,(0, 0))
        window.blit(sp1, (x1, y1))
        window.blit(sp2, (x2, y2)) 
    display.update()
    clock.tick(FPS)