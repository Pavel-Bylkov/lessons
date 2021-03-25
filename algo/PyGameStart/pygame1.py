from pygame import *
from random import randint

win_widht, win_height = 700, 500
window = display.set_mode((win_widht, win_height))
display.set_caption("Догонялки")

background = transform.scale(image.load("background.png"), (win_widht, win_height))

sp1_widht, sp1_height = 50, 50
x1, y1 = 100, 300
speed = 3
sprite1 = transform.scale(image.load('sprite1.png'), (sp1_widht, sp1_height))

sp2_widht, sp2_height = 50, 50
x2, y2 = 300, 400
new_x2, new_y2 = x2, y2
speed2 = 6
sprite2 = transform.scale(image.load('sprite2.png'), (sp2_widht, sp2_height))

clock = time.Clock()
FPS = 60

def is_touching():
    if abs(x1- x2) < sp1_widht - 5 and abs(y1 - y2) < sp1_height - 5:
        return True
    return False

def get_new_pos_sp2():
    global new_x2, new_y2
    if x2 < x1 and x2 > 50 and y2 < y1 and y2 > 50:
        new_x2, new_y2 = randint(0, x2 // 10) * 10, randint(0, y2 // 10) * 10
    elif x2 < x1 and x2 > 50 and y2 > y1 and y2 < win_height - 50:
        new_x2, new_y2 = randint(0, x2 // 10) * 10, randint(y2 // 10, (win_height - 50) // 10) * 10
    elif x2 > x1 and x2 < win_widht - 50 and y2 > y1 and y2 < win_height - 50:
        new_x2, new_y2 = randint(x2 // 10, (win_widht - 50) // 10) * 10, randint(y2 // 10, (win_height - 50) // 10) * 10
    elif x2 > x1 and x2 < win_widht - 50 and y2 < y1 and y2 > 50:
        new_x2, new_y2 = randint(x2 // 10, (win_widht - 50) // 10) * 10, randint(0, y2 // 10) * 10
    else:
        new_x2, new_y2 = randint(0, 65) * 10, randint(0, 45) * 10

def enemy_move():
    global x2, y2, new_x2, new_y2
    if x2 in tuple(range(new_x2 - 10, new_x2 + 10)) and y2 in tuple(range(new_y2 - 10, new_y2 + 10)):
        get_new_pos_sp2()
    dist_x = abs(x1 - x2)
    dist_y = abs(y1 - y2)
    if x2 > new_x2:
       x2 -= speed2
    if x2 < new_x2:
       x2 += speed2
    if y2 > new_y2:
       y2 -= speed2
    if y2 < new_y2:
       y2 += speed2
    if (x2 > 60 and x2 < win_widht - 60 and y2 > 60 and y2 < win_height - 60 
            and dist_x >= abs(x1 - x2) and dist_y >= abs(y1 - y2)):
        get_new_pos_sp2()

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
