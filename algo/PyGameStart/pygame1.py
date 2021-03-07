from pygame import *
from random import randint

win_widht, win_height = 700, 500
window = display.set_mode((win_widht, win_height))
display.set_caption("Догонялки")

background = transform.scale(
    image.load("/home/whector/Documents/GitHub/lessons/algo/PyGameStart/background.png"),
    (win_widht, win_height))
final = transform.scale(
    image.load("/home/whector/Documents/GitHub/lessons/algo/PyGameStart/thumb_1.jpg"),
    (win_widht, win_height))
sp1_widht, sp1_height = 50, 50
x1, y1 = 100, 300
speed = 5
sprite1 = transform.scale(
    image.load('/home/whector/Documents/GitHub/lessons/algo/PyGameStart/sprite1.png'), 
    (sp1_widht, sp1_height))

sp2_widht, sp2_height = 50, 50
x2, y2 = 300, 400
new_x2, new_y2 = x2, y2
speed2 = 1
sprite2 = transform.scale(
    image.load('/home/whector/Documents/GitHub/lessons/algo/PyGameStart/sprite2.png'), 
    (sp2_widht, sp2_height))

clock = time.Clock()
FPS = 60

def is_touching():
    if abs(x1- x2) < sp1_widht - 5 and abs(y1 - y2) < sp1_height - 5:
        return True
    return False

def get_new_pos_sp2():
    global new_x2, new_y2
    if new_x2 == x2 and new_y2 == y2:
       new_x2, new_y2 = randint(1, 65) * 10, randint(1, 45) * 10

def enemy_move():
    global x2, y2
    get_new_pos_sp2()
    if x2 > new_x2:
       x2 -= speed2
    elif x2 < new_x2:
       x2 += speed2
    if y2 > new_y2:
       y2 -= speed2
    elif y2 < new_y2:
       y2 += speed2

def control():
    global x1, y1
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 450:
        y1 += speed

run = True
while run:
    for e in event.get():
        if e.type == QUIT:
          run = False
    if not is_touching():
        control()
        enemy_move()
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    clock.tick(FPS)  # В каждом кадре секунда будет разделена на 60. Будет выполнена задержка на 1/60 секунды.
    display.update()
